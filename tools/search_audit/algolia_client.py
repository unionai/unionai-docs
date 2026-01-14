"""Algolia API client wrapper for search auditing."""

import time
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class SearchHit:
    """A single search result."""

    url: str
    title: str
    position: int  # 1-indexed
    content: str = ""
    hierarchy: dict = field(default_factory=dict)


@dataclass
class SearchResponse:
    """Complete search response with metadata."""

    query: str
    hits: list[SearchHit]
    total_hits: int
    response_time_ms: int
    processing_time_ms: int
    variant_filter: Optional[str] = None
    version_filter: Optional[str] = None


class AlgoliaClient:
    """Wrapper for Algolia search operations."""

    def __init__(
        self,
        app_id: str,
        search_key: str,
        index_name: str,
    ):
        """
        Initialize Algolia client.

        Args:
            app_id: Algolia application ID
            search_key: Algolia search API key (public read-only)
            index_name: Name of the search index
        """
        self.app_id = app_id
        self.search_key = search_key
        self.index_name = index_name
        self._client = None
        self._index = None

    def _get_client(self):
        """Lazy-load the Algolia client."""
        if self._client is None:
            try:
                from algoliasearch.search.client import SearchClientSync

                self._client = SearchClientSync(self.app_id, self.search_key)
            except ImportError:
                raise ImportError(
                    "algoliasearch package required. Install with: pip install algoliasearch"
                )
        return self._client

    def search(
        self,
        query: str,
        variant: Optional[str] = None,
        version: Optional[str] = None,
        hits_per_page: int = 20,
        page: int = 0,
    ) -> SearchResponse:
        """
        Execute a search query against Algolia.

        Args:
            query: Search query string
            variant: Optional variant filter (flyte, byoc, serverless, selfmanaged)
            version: Optional version filter (v1, v2)
            hits_per_page: Number of results per page
            page: Page number (0-indexed)

        Returns:
            SearchResponse with hits and metadata
        """
        client = self._get_client()

        # Build filters
        filters = []
        if variant:
            filters.append(f"variant:{variant}")
        if version:
            filters.append(f"version:{version}")
        filter_string = " AND ".join(filters) if filters else ""

        # Measure response time
        start_time = time.time()

        response = client.search_single_index(
            index_name=self.index_name,
            search_params={
                "query": query,
                "hitsPerPage": hits_per_page,
                "page": page,
                "filters": filter_string,
                "attributesToRetrieve": ["url", "title", "content", "hierarchy"],
            },
        )

        response_time = int((time.time() - start_time) * 1000)

        # Parse hits - handle both dict and Pydantic model responses
        raw_hits = getattr(response, "hits", []) if hasattr(response, "hits") else response.get("hits", [])
        nb_hits = getattr(response, "nb_hits", 0) if hasattr(response, "nb_hits") else response.get("nbHits", 0)
        processing_time = getattr(response, "processing_time_ms", 0) if hasattr(response, "processing_time_ms") else response.get("processingTimeMS", 0)

        hits = []
        for i, hit in enumerate(raw_hits):
            # Convert Pydantic model to dict if needed
            if hasattr(hit, "model_dump"):
                hit_dict = hit.model_dump()
            elif hasattr(hit, "dict"):
                hit_dict = hit.dict()
            elif isinstance(hit, dict):
                hit_dict = hit
            else:
                # Try to access as object with additional_properties
                hit_dict = getattr(hit, "additional_properties", {}) or {}

            url = hit_dict.get("url", "")
            title = hit_dict.get("title", "") or hit_dict.get("hierarchy", {}).get("lvl0", "")
            content = hit_dict.get("content", "")
            hierarchy = hit_dict.get("hierarchy", {})

            # Normalize URL - extract path from full URL if needed
            if url.startswith("http"):
                from urllib.parse import urlparse

                url = urlparse(url).path

            hits.append(
                SearchHit(
                    url=url,
                    title=title,
                    position=i + 1 + (page * hits_per_page),
                    content=content,
                    hierarchy=hierarchy,
                )
            )

        return SearchResponse(
            query=query,
            hits=hits,
            total_hits=nb_hits,
            response_time_ms=response_time,
            processing_time_ms=processing_time,
            variant_filter=variant,
            version_filter=version,
        )

    def get_index_stats(self) -> dict[str, Any]:
        """Get index statistics."""
        client = self._get_client()
        settings = client.get_settings(index_name=self.index_name)
        return {
            "index_name": self.index_name,
            "settings": settings,
        }
