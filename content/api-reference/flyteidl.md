---
title: Flyteidl
variants: -byoc -selfmanaged -serverless +flyte
weight: 5
---

# Flyteidl



## flyteidl/core/compiler.proto




### CompiledLaunchPlan {#flyteidl-core-CompiledLaunchPlan}
Output of the compilation step. This object represents one LaunchPlan. We store more metadata at this layer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| template | [LaunchPlanTemplate](#flyteidl-core-LaunchPlanTemplate) |  | Completely contained LaunchPlan Template |







### CompiledTask {#flyteidl-core-CompiledTask}
Output of the Compilation step. This object represent one Task. We store more metadata at this layer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| template | [TaskTemplate](#flyteidl-core-TaskTemplate) |  | Completely contained TaskTemplate |







### CompiledWorkflow {#flyteidl-core-CompiledWorkflow}
Output of the compilation Step. This object represents one workflow. We store more metadata at this layer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| template | [WorkflowTemplate](#flyteidl-core-WorkflowTemplate) |  | Completely contained Workflow Template |
| connections | [ConnectionSet](#flyteidl-core-ConnectionSet) |  | For internal use only! This field is used by the system and must not be filled in. Any values set will be ignored. |







### CompiledWorkflowClosure {#flyteidl-core-CompiledWorkflowClosure}
A Compiled Workflow Closure contains all the information required to start a new execution, or to visualize a workflow
and its details. The CompiledWorkflowClosure should always contain a primary workflow, that is the main workflow that
will being the execution. All subworkflows are denormalized. WorkflowNodes refer to the workflow identifiers of
compiled subworkflows.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| primary | [CompiledWorkflow](#flyteidl-core-CompiledWorkflow) |  | +required |
| sub_workflows | [CompiledWorkflow](#flyteidl-core-CompiledWorkflow) | repeated | Guaranteed that there will only exist one and only one workflow with a given id, i.e., every sub workflow has a unique identifier. Also every enclosed subworkflow is used either by a primary workflow or by a subworkflow as an inlined workflow +optional |
| tasks | [CompiledTask](#flyteidl-core-CompiledTask) | repeated | Guaranteed that there will only exist one and only one task with a given id, i.e., every task has a unique id +required (at least 1) |
| launch_plans | [CompiledLaunchPlan](#flyteidl-core-CompiledLaunchPlan) | repeated | A collection of launch plans that are compiled. Guaranteed that there will only exist one and only one launch plan with a given id, i.e., every launch plan has a unique id. |







### ConnectionSet {#flyteidl-core-ConnectionSet}
Adjacency list for the workflow. This is created as part of the compilation process. Every process after the compilation
step uses this created ConnectionSet



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| downstream | [ConnectionSet.DownstreamEntry](#flyteidl-core-ConnectionSet-DownstreamEntry) | repeated | A list of all the node ids that are downstream from a given node id |
| upstream | [ConnectionSet.UpstreamEntry](#flyteidl-core-ConnectionSet-UpstreamEntry) | repeated | A list of all the node ids, that are upstream of this node id |







### ConnectionSet.DownstreamEntry {#flyteidl-core-ConnectionSet-DownstreamEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | [ConnectionSet.IdList](#flyteidl-core-ConnectionSet-IdList) |  |  |







### ConnectionSet.IdList {#flyteidl-core-ConnectionSet-IdList}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ids | string | repeated |  |







### ConnectionSet.UpstreamEntry {#flyteidl-core-ConnectionSet-UpstreamEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | [ConnectionSet.IdList](#flyteidl-core-ConnectionSet-IdList) |  |  |
















## flyteidl/core/interface.proto




### Parameter {#flyteidl-core-Parameter}
A parameter is used as input to a launch plan and has
the special ability to have a default value or mark itself as required.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| var | [Variable](#flyteidl-core-Variable) |  | +required Variable. Defines the type of the variable backing this parameter. |
| default | [Literal](#flyteidl-core-Literal) |  | Defines a default value that has to match the variable type defined. |
| required | bool |  | +optional, is this value required to be filled. |
| artifact_query | [ArtifactQuery](#flyteidl-core-ArtifactQuery) |  | This is an execution time search basically that should result in exactly one Artifact with a Type that matches the type of the variable. |
| artifact_id | [ArtifactID](#flyteidl-core-ArtifactID) |  |  |







### ParameterMap {#flyteidl-core-ParameterMap}
A map of Parameters.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| parameters | [ParameterMap.ParametersEntry](#flyteidl-core-ParameterMap-ParametersEntry) | repeated | Defines a map of parameter names to parameters. |







### ParameterMap.ParametersEntry {#flyteidl-core-ParameterMap-ParametersEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | [Parameter](#flyteidl-core-Parameter) |  |  |







### TypedInterface {#flyteidl-core-TypedInterface}
Defines strongly typed inputs and outputs.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inputs | [VariableMap](#flyteidl-core-VariableMap) |  |  |
| outputs | [VariableMap](#flyteidl-core-VariableMap) |  |  |







### Variable {#flyteidl-core-Variable}
Defines a strongly typed variable.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [LiteralType](#flyteidl-core-LiteralType) |  | Variable literal type. |
| description | string |  | +optional string describing input variable |
| artifact_partial_id | [ArtifactID](#flyteidl-core-ArtifactID) |  | +optional This object allows the user to specify how Artifacts are created. name, tag, partitions can be specified. The other fields (version and project/domain) are ignored. |
| artifact_tag | [ArtifactTag](#flyteidl-core-ArtifactTag) |  |  |







### VariableMap {#flyteidl-core-VariableMap}
A map of Variables



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| variables | [VariableMap.VariablesEntry](#flyteidl-core-VariableMap-VariablesEntry) | repeated | Defines a map of variable names to variables. |







### VariableMap.VariablesEntry {#flyteidl-core-VariableMap-VariablesEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | [Variable](#flyteidl-core-Variable) |  |  |
















## flyteidl/core/catalog.proto




### CatalogArtifactTag {#flyteidl-core-CatalogArtifactTag}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact_id | string |  | Artifact ID is generated name |
| name | string |  | Flyte computes the tag automatically, as the hash of the values |







### CatalogMetadata {#flyteidl-core-CatalogMetadata}
Catalog artifact information with specific metadata



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dataset_id | [Identifier](#flyteidl-core-Identifier) |  | Dataset ID in the catalog |
| artifact_tag | [CatalogArtifactTag](#flyteidl-core-CatalogArtifactTag) |  | Artifact tag in the catalog |
| source_task_execution | [TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  | Today we only support TaskExecutionIdentifier as a source, as catalog caching only works for task executions |







### CatalogReservation {#flyteidl-core-CatalogReservation}










### CatalogCacheStatus {#flyteidl-core-CatalogCacheStatus}
Indicates the status of CatalogCaching. The reason why this is not embedded in TaskNodeMetadata is, that we may use for other types of nodes as well in the future

| Name | Number | Description |
| ---- | ------ | ----------- |
| CACHE_DISABLED | 0 | Used to indicate that caching was disabled |
| CACHE_MISS | 1 | Used to indicate that the cache lookup resulted in no matches |
| CACHE_HIT | 2 | used to indicate that the associated artifact was a result of a previous execution |
| CACHE_POPULATED | 3 | used to indicate that the resultant artifact was added to the cache |
| CACHE_LOOKUP_FAILURE | 4 | Used to indicate that cache lookup failed because of an error |
| CACHE_PUT_FAILURE | 5 | Used to indicate that cache lookup failed because of an error |
| CACHE_SKIPPED | 6 | Used to indicate the cache lookup was skipped |
| CACHE_EVICTED | 7 | Used to indicate that the cache was evicted |




### CatalogReservation.Status {#flyteidl-core-CatalogReservation-Status}
Indicates the status of a catalog reservation operation.

| Name | Number | Description |
| ---- | ------ | ----------- |
| RESERVATION_DISABLED | 0 | Used to indicate that reservations are disabled |
| RESERVATION_ACQUIRED | 1 | Used to indicate that a reservation was successfully acquired or extended |
| RESERVATION_EXISTS | 2 | Used to indicate that an active reservation currently exists |
| RESERVATION_RELEASED | 3 | Used to indicate that the reservation has been successfully released |
| RESERVATION_FAILURE | 4 | Used to indicate that a reservation operation resulted in failure |











## flyteidl/core/literals.proto




### Binary {#flyteidl-core-Binary}
A simple byte array with a tag to help different parts of the system communicate about what is in the byte array.
It's strongly advisable that consumers of this type define a unique tag and validate the tag before parsing the data.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | bytes |  | Serialized data (MessagePack) for supported types like Dataclass, Pydantic BaseModel, and untyped dict. |
| tag | string |  | The serialization format identifier (e.g., MessagePack). Consumers must define unique tags and validate them before deserialization. |







### Binding {#flyteidl-core-Binding}
An input/output binding of a variable to either static value or a node output.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| var | string |  | Variable name must match an input/output variable of the node. |
| binding | [BindingData](#flyteidl-core-BindingData) |  | Data to use to bind this variable. |







### BindingData {#flyteidl-core-BindingData}
Specifies either a simple value or a reference to another output.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| scalar | [Scalar](#flyteidl-core-Scalar) |  | A simple scalar value. |
| collection | [BindingDataCollection](#flyteidl-core-BindingDataCollection) |  | A collection of binding data. This allows nesting of binding data to any number of levels. |
| promise | [OutputReference](#flyteidl-core-OutputReference) |  | References an output promised by another node. |
| map | [BindingDataMap](#flyteidl-core-BindingDataMap) |  | A map of bindings. The key is always a string. |
| offloaded_metadata | [LiteralOffloadedMetadata](#flyteidl-core-LiteralOffloadedMetadata) |  | Offloaded literal metadata When you deserialize the offloaded metadata, it would be of Literal and its type would be defined by LiteralType stored in offloaded_metadata. Used for nodes that don't have promises from upstream nodes such as ArrayNode subNodes. |
| union | [UnionInfo](#flyteidl-core-UnionInfo) |  |  |







### BindingDataCollection {#flyteidl-core-BindingDataCollection}
A collection of BindingData items.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bindings | [BindingData](#flyteidl-core-BindingData) | repeated |  |







### BindingDataMap {#flyteidl-core-BindingDataMap}
A map of BindingData items.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bindings | [BindingDataMap.BindingsEntry](#flyteidl-core-BindingDataMap-BindingsEntry) | repeated |  |







### BindingDataMap.BindingsEntry {#flyteidl-core-BindingDataMap-BindingsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | [BindingData](#flyteidl-core-BindingData) |  |  |







### Blob {#flyteidl-core-Blob}
Refers to an offloaded set of files. It encapsulates the type of the store and a unique uri for where the data is.
There are no restrictions on how the uri is formatted since it will depend on how to interact with the store.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| metadata | [BlobMetadata](#flyteidl-core-BlobMetadata) |  |  |
| uri | string |  |  |







### BlobMetadata {#flyteidl-core-BlobMetadata}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [BlobType](#flyteidl-core-BlobType) |  |  |







### KeyValuePair {#flyteidl-core-KeyValuePair}
A generic key value pair.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  | required. |
| value | string |  | +optional. |







### Literal {#flyteidl-core-Literal}
A simple value. This supports any level of nesting (e.g. array of array of array of Blobs) as well as simple primitives.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| scalar | [Scalar](#flyteidl-core-Scalar) |  | A simple value. |
| collection | [LiteralCollection](#flyteidl-core-LiteralCollection) |  | A collection of literals to allow nesting. |
| map | [LiteralMap](#flyteidl-core-LiteralMap) |  | A map of strings to literals. |
| offloaded_metadata | [LiteralOffloadedMetadata](#flyteidl-core-LiteralOffloadedMetadata) |  | Offloaded literal metadata When you deserialize the offloaded metadata, it would be of Literal and its type would be defined by LiteralType stored in offloaded_metadata. |
| hash | string |  | A hash representing this literal. This is used for caching purposes. For more details refer to RFC 1893 (https://github.com/flyteorg/flyte/blob/master/rfc/system/1893-caching-of-offloaded-objects.md) |
| metadata | [Literal.MetadataEntry](#flyteidl-core-Literal-MetadataEntry) | repeated | Additional metadata for literals. |







### Literal.MetadataEntry {#flyteidl-core-Literal-MetadataEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### LiteralCollection {#flyteidl-core-LiteralCollection}
A collection of literals. This is a workaround since oneofs in proto messages cannot contain a repeated field.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| literals | [Literal](#flyteidl-core-Literal) | repeated |  |







### LiteralMap {#flyteidl-core-LiteralMap}
A map of literals. This is a workaround since oneofs in proto messages cannot contain a repeated field.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| literals | [LiteralMap.LiteralsEntry](#flyteidl-core-LiteralMap-LiteralsEntry) | repeated |  |







### LiteralMap.LiteralsEntry {#flyteidl-core-LiteralMap-LiteralsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | [Literal](#flyteidl-core-Literal) |  |  |







### LiteralOffloadedMetadata {#flyteidl-core-LiteralOffloadedMetadata}
A message that contains the metadata of the offloaded data.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uri | string |  | The location of the offloaded core.Literal. |
| size_bytes | uint64 |  | The size of the offloaded data. |
| inferred_type | [LiteralType](#flyteidl-core-LiteralType) |  | The inferred literal type of the offloaded data. |







### Primitive {#flyteidl-core-Primitive}
Primitive Types



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| integer | int64 |  |  |
| float_value | double |  |  |
| string_value | string |  |  |
| boolean | bool |  |  |
| datetime | google.protobuf.Timestamp |  |  |
| duration | google.protobuf.Duration |  |  |







### RetryStrategy {#flyteidl-core-RetryStrategy}
Retry strategy associated with an executable unit.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| retries | uint32 |  | Number of retries. Retries will be consumed when the job fails with a recoverable error. The number of retries must be less than or equals to 10. |







### Scalar {#flyteidl-core-Scalar}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| primitive | [Primitive](#flyteidl-core-Primitive) |  |  |
| blob | [Blob](#flyteidl-core-Blob) |  |  |
| binary | [Binary](#flyteidl-core-Binary) |  |  |
| schema | [Schema](#flyteidl-core-Schema) |  |  |
| none_type | [Void](#flyteidl-core-Void) |  |  |
| error | [Error](#flyteidl-core-Error) |  |  |
| generic | google.protobuf.Struct |  |  |
| structured_dataset | [StructuredDataset](#flyteidl-core-StructuredDataset) |  |  |
| union | [Union](#flyteidl-core-Union) |  |  |







### Schema {#flyteidl-core-Schema}
A strongly typed schema that defines the interface of data retrieved from the underlying storage medium.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uri | string |  |  |
| type | [SchemaType](#flyteidl-core-SchemaType) |  |  |







### StructuredDataset {#flyteidl-core-StructuredDataset}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uri | string |  | String location uniquely identifying where the data is. Should start with the storage location (e.g. s3://, gs://, bq://, etc.) |
| metadata | [StructuredDatasetMetadata](#flyteidl-core-StructuredDatasetMetadata) |  |  |







### StructuredDatasetMetadata {#flyteidl-core-StructuredDatasetMetadata}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| structured_dataset_type | [StructuredDatasetType](#flyteidl-core-StructuredDatasetType) |  | Bundle the type information along with the literal. This is here because StructuredDatasets can often be more defined at run time than at compile time. That is, at compile time you might only declare a task to return a pandas dataframe or a StructuredDataset, without any column information, but at run time, you might have that column information. flytekit python will copy this type information into the literal, from the type information, if not provided by the various plugins (encoders). Since this field is run time generated, it's not used for any type checking. |







### Union {#flyteidl-core-Union}
The runtime representation of a tagged union value. See `UnionType` for more details.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [Literal](#flyteidl-core-Literal) |  |  |
| type | [LiteralType](#flyteidl-core-LiteralType) |  |  |







### UnionInfo {#flyteidl-core-UnionInfo}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| targetType | [LiteralType](#flyteidl-core-LiteralType) |  |  |







### Void {#flyteidl-core-Void}
Used to denote a nil/null/None assignment to a scalar value. The underlying LiteralType for Void is intentionally
undefined since it can be assigned to a scalar of any LiteralType.
















## flyteidl/core/tasks.proto




### Container {#flyteidl-core-Container}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| image | string |  | Container image url. Eg: docker/redis:latest |
| command | string | repeated | Command to be executed, if not provided, the default entrypoint in the container image will be used. |
| args | string | repeated | These will default to Flyte given paths. If provided, the system will not append known paths. If the task still needs flyte's inputs and outputs path, add $(FLYTE_INPUT_FILE), $(FLYTE_OUTPUT_FILE) wherever makes sense and the system will populate these before executing the container. |
| resources | [Resources](#flyteidl-core-Resources) |  | Container resources requirement as specified by the container engine. |
| env | [KeyValuePair](#flyteidl-core-KeyValuePair) | repeated | Environment variables will be set as the container is starting up. |
| config | [KeyValuePair](#flyteidl-core-KeyValuePair) | repeated | **Deprecated.** Allows extra configs to be available for the container. TODO: elaborate on how configs will become available. Deprecated, please use TaskTemplate.config instead. |
| ports | [ContainerPort](#flyteidl-core-ContainerPort) | repeated | Ports to open in the container. This feature is not supported by all execution engines. (e.g. supported on K8s but not supported on AWS Batch) Only K8s |
| data_config | [DataLoadingConfig](#flyteidl-core-DataLoadingConfig) |  | BETA: Optional configuration for DataLoading. If not specified, then default values are used. This makes it possible to to run a completely portable container, that uses inputs and outputs only from the local file-system and without having any reference to flyteidl. This is supported only on K8s at the moment. If data loading is enabled, then data will be mounted in accompanying directories specified in the DataLoadingConfig. If the directories are not specified, inputs will be mounted onto and outputs will be uploaded from a pre-determined file-system path. Refer to the documentation to understand the default paths. Only K8s |
| architecture | [Container.Architecture](#flyteidl-core-Container-Architecture) |  |  |







### ContainerPort {#flyteidl-core-ContainerPort}
Defines port properties for a container.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| container_port | uint32 |  | Number of port to expose on the pod's IP address. This must be a valid port number, 0 <lt; x <lt; 65536. |
| name | string |  | Name of the port to expose on the pod's IP address. |







### DataLoadingConfig {#flyteidl-core-DataLoadingConfig}
This configuration allows executing raw containers in Flyte using the Flyte CoPilot system.
Flyte CoPilot, eliminates the needs of flytekit or sdk inside the container. Any inputs required by the users container are side-loaded in the input_path
Any outputs generated by the user container - within output_path are automatically uploaded.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| enabled | bool |  | Flag enables DataLoading Config. If this is not set, data loading will not be used! |
| input_path | string |  | File system path (start at root). This folder will contain all the inputs exploded to a separate file. Example, if the input interface needs (x: int, y: blob, z: multipart_blob) and the input path is '/var/flyte/inputs', then the file system will look like /var/flyte/inputs/inputs.<lt;metadata format dependent ->gt; .pb .json .yaml>gt; ->gt; Format as defined previously. The Blob and Multipart blob will reference local filesystem instead of remote locations /var/flyte/inputs/x ->gt; X is a file that contains the value of x (integer) in string format /var/flyte/inputs/y ->gt; Y is a file in Binary format /var/flyte/inputs/z/... ->gt; Note Z itself is a directory More information about the protocol - refer to docs #TODO reference docs here |
| output_path | string |  | File system path (start at root). This folder should contain all the outputs for the task as individual files and/or an error text file |
| format | [DataLoadingConfig.LiteralMapFormat](#flyteidl-core-DataLoadingConfig-LiteralMapFormat) |  | In the inputs folder, there will be an additional summary/metadata file that contains references to all files or inlined primitive values. This format decides the actual encoding for the data. Refer to the encoding to understand the specifics of the contents and the encoding |
| io_strategy | [IOStrategy](#flyteidl-core-IOStrategy) |  |  |







### ExtendedResources {#flyteidl-core-ExtendedResources}
Encapsulates all non-standard resources, not captured by v1.ResourceRequirements, to
allocate to a task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gpu_accelerator | [GPUAccelerator](#flyteidl-core-GPUAccelerator) |  | GPU accelerator to select for task. Contains information about device type, and for multi-instance GPUs, the partition size to use. |
| shared_memory | [SharedMemory](#flyteidl-core-SharedMemory) |  |  |







### GPUAccelerator {#flyteidl-core-GPUAccelerator}
Metadata associated with the GPU accelerator to allocate to a task. Contains
information about device type, and for multi-instance GPUs, the partition size to
use.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| device | string |  | This can be any arbitrary string, and should be informed by the labels or taints associated with the nodes in question. Default cloud provider labels typically use the following values: `nvidia-tesla-t4`, `nvidia-tesla-a100`, etc. |
| unpartitioned | bool |  |  |
| partition_size | string |  | Like `device`, this can be any arbitrary string, and should be informed by the labels or taints associated with the nodes in question. Default cloud provider labels typically use the following values: `1g.5gb`, `2g.10gb`, etc. |







### IOStrategy {#flyteidl-core-IOStrategy}
Strategy to use when dealing with Blob, Schema, or multipart blob data (large datasets)



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| download_mode | [IOStrategy.DownloadMode](#flyteidl-core-IOStrategy-DownloadMode) |  | Mode to use to manage downloads |
| upload_mode | [IOStrategy.UploadMode](#flyteidl-core-IOStrategy-UploadMode) |  | Mode to use to manage uploads |







### K8sObjectMetadata {#flyteidl-core-K8sObjectMetadata}
Metadata for building a kubernetes object when a task is executed.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| labels | [K8sObjectMetadata.LabelsEntry](#flyteidl-core-K8sObjectMetadata-LabelsEntry) | repeated | Optional labels to add to the pod definition. |
| annotations | [K8sObjectMetadata.AnnotationsEntry](#flyteidl-core-K8sObjectMetadata-AnnotationsEntry) | repeated | Optional annotations to add to the pod definition. |







### K8sObjectMetadata.AnnotationsEntry {#flyteidl-core-K8sObjectMetadata-AnnotationsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### K8sObjectMetadata.LabelsEntry {#flyteidl-core-K8sObjectMetadata-LabelsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### K8sPod {#flyteidl-core-K8sPod}
Defines a pod spec and additional pod metadata that is created when a task is executed.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| metadata | [K8sObjectMetadata](#flyteidl-core-K8sObjectMetadata) |  | Contains additional metadata for building a kubernetes pod. |
| pod_spec | google.protobuf.Struct |  | Defines the primary pod spec created when a task is executed. This should be a JSON-marshalled pod spec, which can be defined in - go, using: https://github.com/kubernetes/api/blob/release-1.21/core/v1/types.go#L2936 - python: using https://github.com/kubernetes-client/python/blob/release-19.0/kubernetes/client/models/v1_pod_spec.py |
| data_config | [DataLoadingConfig](#flyteidl-core-DataLoadingConfig) |  | BETA: Optional configuration for DataLoading. If not specified, then default values are used. This makes it possible to to run a completely portable container, that uses inputs and outputs only from the local file-system and without having any reference to flytekit. This is supported only on K8s at the moment. If data loading is enabled, then data will be mounted in accompanying directories specified in the DataLoadingConfig. If the directories are not specified, inputs will be mounted onto and outputs will be uploaded from a pre-determined file-system path. Refer to the documentation to understand the default paths. Only K8s |
| primary_container_name | string |  | Defines the primary container name when pod template override is executed. |







### Resources {#flyteidl-core-Resources}
A customizable interface to convey resources requested for a container. This can be interpreted differently for different
container engines.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| requests | [Resources.ResourceEntry](#flyteidl-core-Resources-ResourceEntry) | repeated | The desired set of resources requested. ResourceNames must be unique within the list. |
| limits | [Resources.ResourceEntry](#flyteidl-core-Resources-ResourceEntry) | repeated | Defines a set of bounds (e.g. min/max) within which the task can reliably run. ResourceNames must be unique within the list. |







### Resources.ResourceEntry {#flyteidl-core-Resources-ResourceEntry}
Encapsulates a resource name and value.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [Resources.ResourceName](#flyteidl-core-Resources-ResourceName) |  | Resource name. |
| value | string |  | Value must be a valid k8s quantity. See https://github.com/kubernetes/apimachinery/blob/master/pkg/api/resource/quantity.go#L30-L80 |







### RuntimeMetadata {#flyteidl-core-RuntimeMetadata}
Runtime information. This is loosely defined to allow for extensibility.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [RuntimeMetadata.RuntimeType](#flyteidl-core-RuntimeMetadata-RuntimeType) |  | Type of runtime. |
| version | string |  | Version of the runtime. All versions should be backward compatible. However, certain cases call for version checks to ensure tighter validation or setting expectations. |
| flavor | string |  | +optional It can be used to provide extra information about the runtime (e.g. python, golang... etc.). |







### SharedMemory {#flyteidl-core-SharedMemory}
Metadata associated with configuring a shared memory volume for a task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mount_path | string |  | Mount path to place in container |
| mount_name | string |  | Name for volume |
| size_limit | string |  | Size limit for shared memory. If not set, then the shared memory is equal to the allocated memory. +optional |







### Sql {#flyteidl-core-Sql}
Sql represents a generic sql workload with a statement and dialect.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| statement | string |  | The actual query to run, the query can have templated parameters. We use Flyte's Golang templating format for Query templating. For example, insert overwrite directory '{{ .rawOutputDataPrefix }}' stored as parquet select * from my_table where ds = '{{ .Inputs.ds }}' |
| dialect | [Sql.Dialect](#flyteidl-core-Sql-Dialect) |  |  |







### TaskMetadata {#flyteidl-core-TaskMetadata}
Task Metadata



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| discoverable | bool |  | Indicates whether the system should attempt to lookup this task's output to avoid duplication of work. |
| runtime | [RuntimeMetadata](#flyteidl-core-RuntimeMetadata) |  | Runtime information about the task. |
| timeout | google.protobuf.Duration |  | The overall timeout of a task including user-triggered retries. |
| retries | [RetryStrategy](#flyteidl-core-RetryStrategy) |  | Number of retries per task. |
| discovery_version | string |  | Indicates a logical version to apply to this task for the purpose of discovery. |
| deprecated_error_message | string |  | If set, this indicates that this task is deprecated. This will enable owners of tasks to notify consumers of the ending of support for a given task. |
| interruptible | bool |  |  |
| cache_serializable | bool |  | Indicates whether the system should attempt to execute discoverable instances in serial to avoid duplicate work |
| tags | [TaskMetadata.TagsEntry](#flyteidl-core-TaskMetadata-TagsEntry) | repeated | Arbitrary tags that allow users and the platform to store small but arbitrary labels |
| pod_template_name | string |  | pod_template_name is the unique name of a PodTemplate k8s resource to be used as the base configuration if this task creates a k8s Pod. If this value is set, the specified PodTemplate will be used instead of, but applied identically as, the default PodTemplate configured in FlytePropeller. |
| cache_ignore_input_vars | string | repeated | cache_ignore_input_vars is the input variables that should not be included when calculating hash for cache. |
| is_eager | bool |  | is_eager indicates whether the task is eager or not. This would be used by CreateTask endpoint. |
| generates_deck | google.protobuf.BoolValue |  | Indicates whether the task will generate a deck when it finishes executing. The BoolValue can have three states: - nil: The value is not set. - true: The task will generate a deck. - false: The task will not generate a deck. |







### TaskMetadata.TagsEntry {#flyteidl-core-TaskMetadata-TagsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### TaskTemplate {#flyteidl-core-TaskTemplate}
A Task structure that uniquely identifies a task in the system
Tasks are registered as a first step in the system.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [Identifier](#flyteidl-core-Identifier) |  | Auto generated taskId by the system. Task Id uniquely identifies this task globally. |
| type | string |  | A predefined yet extensible Task type identifier. This can be used to customize any of the components. If no extensions are provided in the system, Flyte will resolve the this task to its TaskCategory and default the implementation registered for the TaskCategory. |
| metadata | [TaskMetadata](#flyteidl-core-TaskMetadata) |  | Extra metadata about the task. |
| interface | [TypedInterface](#flyteidl-core-TypedInterface) |  | A strongly typed interface for the task. This enables others to use this task within a workflow and guarantees compile-time validation of the workflow to avoid costly runtime failures. |
| custom | google.protobuf.Struct |  | Custom data about the task. This is extensible to allow various plugins in the system. |
| container | [Container](#flyteidl-core-Container) |  |  |
| k8s_pod | [K8sPod](#flyteidl-core-K8sPod) |  |  |
| sql | [Sql](#flyteidl-core-Sql) |  |  |
| task_type_version | int32 |  | This can be used to customize task handling at execution time for the same task type. |
| security_context | [SecurityContext](#flyteidl-core-SecurityContext) |  | security_context encapsulates security attributes requested to run this task. |
| extended_resources | [ExtendedResources](#flyteidl-core-ExtendedResources) |  | Encapsulates all non-standard resources, not captured by v1.ResourceRequirements, to allocate to a task. |
| config | [TaskTemplate.ConfigEntry](#flyteidl-core-TaskTemplate-ConfigEntry) | repeated | Metadata about the custom defined for this task. This is extensible to allow various plugins in the system to use as required. reserve the field numbers 1 through 15 for very frequently occurring message elements |







### TaskTemplate.ConfigEntry {#flyteidl-core-TaskTemplate-ConfigEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |









### Container.Architecture {#flyteidl-core-Container-Architecture}
Architecture-type the container image supports.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| AMD64 | 1 |  |
| ARM64 | 2 |  |
| ARM_V6 | 3 |  |
| ARM_V7 | 4 |  |




### DataLoadingConfig.LiteralMapFormat {#flyteidl-core-DataLoadingConfig-LiteralMapFormat}
LiteralMapFormat decides the encoding format in which the input metadata should be made available to the containers.
If the user has access to the protocol buffer definitions, it is recommended to use the PROTO format.
JSON and YAML do not need any protobuf definitions to read it
All remote references in core.LiteralMap are replaced with local filesystem references (the data is downloaded to local filesystem)

| Name | Number | Description |
| ---- | ------ | ----------- |
| JSON | 0 | JSON / YAML for the metadata (which contains inlined primitive values). The representation is inline with the standard json specification as specified - https://www.json.org/json-en.html |
| YAML | 1 |  |
| PROTO | 2 | Proto is a serialized binary of `core.LiteralMap` defined in flyteidl/core |




### IOStrategy.DownloadMode {#flyteidl-core-IOStrategy-DownloadMode}
Mode to use for downloading

| Name | Number | Description |
| ---- | ------ | ----------- |
| DOWNLOAD_EAGER | 0 | All data will be downloaded before the main container is executed |
| DOWNLOAD_STREAM | 1 | Data will be downloaded as a stream and an End-Of-Stream marker will be written to indicate all data has been downloaded. Refer to protocol for details |
| DO_NOT_DOWNLOAD | 2 | Large objects (offloaded) will not be downloaded |




### IOStrategy.UploadMode {#flyteidl-core-IOStrategy-UploadMode}
Mode to use for uploading

| Name | Number | Description |
| ---- | ------ | ----------- |
| UPLOAD_ON_EXIT | 0 | All data will be uploaded after the main container exits |
| UPLOAD_EAGER | 1 | Data will be uploaded as it appears. Refer to protocol specification for details |
| DO_NOT_UPLOAD | 2 | Data will not be uploaded, only references will be written |




### Resources.ResourceName {#flyteidl-core-Resources-ResourceName}
Known resource names.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| CPU | 1 |  |
| GPU | 2 |  |
| MEMORY | 3 |  |
| STORAGE | 4 |  |
| EPHEMERAL_STORAGE | 5 | For Kubernetes-based deployments, pods use ephemeral local storage for scratch space, caching, and for logs. |




### RuntimeMetadata.RuntimeType {#flyteidl-core-RuntimeMetadata-RuntimeType}


| Name | Number | Description |
| ---- | ------ | ----------- |
| OTHER | 0 |  |
| FLYTE_SDK | 1 |  |




### Sql.Dialect {#flyteidl-core-Sql-Dialect}
The dialect of the SQL statement. This is used to validate and parse SQL statements at compilation time to avoid
expensive runtime operations. If set to an unsupported dialect, no validation will be done on the statement.
We support the following dialect: ansi, hive.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED | 0 |  |
| ANSI | 1 |  |
| HIVE | 2 |  |
| OTHER | 3 |  |











## flyteidl/core/metrics.proto




### ExecutionMetricResult {#flyteidl-core-ExecutionMetricResult}
ExecutionMetrics is a collection of metrics that are collected during the execution of a Flyte task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| metric | string |  | The metric this data represents. e.g. EXECUTION_METRIC_USED_CPU_AVG or EXECUTION_METRIC_USED_MEMORY_BYTES_AVG. |
| data | google.protobuf.Struct |  | The result data in prometheus range query result format https://prometheus.io/docs/prometheus/latest/querying/api/#expression-query-result-formats. This may include multiple time series, differentiated by their metric labels. Start time is greater of (execution attempt start, 48h ago) End time is lesser of (execution attempt end, now) |







### Span {#flyteidl-core-Span}
Span represents a duration trace of Flyte execution. The id field denotes a Flyte execution entity or an operation
which uniquely identifies the Span. The spans attribute allows this Span to be further broken down into more
precise definitions.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start_time | google.protobuf.Timestamp |  | start_time defines the instance this span began. |
| end_time | google.protobuf.Timestamp |  | end_time defines the instance this span completed. |
| workflow_id | [WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | workflow_id is the id of the workflow execution this Span represents. |
| node_id | [NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | node_id is the id of the node execution this Span represents. |
| task_id | [TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  | task_id is the id of the task execution this Span represents. |
| operation_id | string |  | operation_id is the id of a unique operation that this Span represents. |
| spans | [Span](#flyteidl-core-Span) | repeated | spans defines a collection of Spans that breakdown this execution. |
















## flyteidl/core/errors.proto




### ContainerError {#flyteidl-core-ContainerError}
Error message to propagate detailed errors from container executions to the execution
engine.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | string |  | A simplified code for errors, so that we can provide a glossary of all possible errors. |
| message | string |  | A detailed error message. |
| kind | [ContainerError.Kind](#flyteidl-core-ContainerError-Kind) |  | An abstract error kind for this error. Defaults to Non_Recoverable if not specified. |
| origin | [ExecutionError.ErrorKind](#flyteidl-core-ExecutionError-ErrorKind) |  | Defines the origin of the error (system, user, unknown). |
| timestamp | google.protobuf.Timestamp |  | Timestamp of the error |
| worker | string |  | Worker that generated the error |







### ErrorDocument {#flyteidl-core-ErrorDocument}
Defines the errors.pb file format the container can produce to communicate
failure reasons to the execution engine.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [ContainerError](#flyteidl-core-ContainerError) |  | The error raised during execution. |









### ContainerError.Kind {#flyteidl-core-ContainerError-Kind}
Defines a generic error type that dictates the behavior of the retry strategy.

| Name | Number | Description |
| ---- | ------ | ----------- |
| NON_RECOVERABLE | 0 |  |
| RECOVERABLE | 1 |  |











## flyteidl/core/identifier.proto




### Identifier {#flyteidl-core-Identifier}
Encapsulation of fields that uniquely identifies a Flyte resource.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_type | [ResourceType](#flyteidl-core-ResourceType) |  | Identifies the specific type of resource that this identifier corresponds to. |
| project | string |  | Name of the project the resource belongs to. |
| domain | string |  | Name of the domain the resource belongs to. A domain can be considered as a subset within a specific project. |
| name | string |  | User provided value for the resource. |
| version | string |  | Specific version of the resource. |
| org | string |  | Optional, org key applied to the resource. |







### NodeExecutionIdentifier {#flyteidl-core-NodeExecutionIdentifier}
Encapsulation of fields that identify a Flyte node execution entity.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_id | string |  |  |
| execution_id | [WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  |  |







### SignalIdentifier {#flyteidl-core-SignalIdentifier}
Encapsulation of fields the uniquely identify a signal.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signal_id | string |  | Unique identifier for a signal. |
| execution_id | [WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Identifies the Flyte workflow execution this signal belongs to. |







### TaskExecutionIdentifier {#flyteidl-core-TaskExecutionIdentifier}
Encapsulation of fields that identify a Flyte task execution entity.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [Identifier](#flyteidl-core-Identifier) |  |  |
| node_execution_id | [NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  |  |
| retry_attempt | uint32 |  |  |







### WorkflowExecutionIdentifier {#flyteidl-core-WorkflowExecutionIdentifier}
Encapsulation of fields that uniquely identifies a Flyte workflow execution



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Name of the project the resource belongs to. |
| domain | string |  | Name of the domain the resource belongs to. A domain can be considered as a subset within a specific project. |
| name | string |  | User or system provided value for the resource. |
| org | string |  | Optional, org key applied to the resource. |









### ResourceType {#flyteidl-core-ResourceType}
Indicates a resource type within Flyte.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSPECIFIED | 0 |  |
| TASK | 1 |  |
| WORKFLOW | 2 |  |
| LAUNCH_PLAN | 3 |  |
| DATASET | 4 | A dataset represents an entity modeled in Flyte DataCatalog. A Dataset is also a versioned entity and can be a compilation of multiple individual objects. Eventually all Catalog objects should be modeled similar to Flyte Objects. The Dataset entities makes it possible for the UI and CLI to act on the objects in a similar manner to other Flyte objects |











## flyteidl/core/artifact_id.proto




### ArtifactBindingData {#flyteidl-core-ArtifactBindingData}
Only valid for triggers



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| partition_key | string |  |  |
| bind_to_time_partition | bool |  |  |
| time_transform | [TimeTransform](#flyteidl-core-TimeTransform) |  | This is only relevant in the time partition case |







### ArtifactID {#flyteidl-core-ArtifactID}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact_key | [ArtifactKey](#flyteidl-core-ArtifactKey) |  |  |
| version | string |  |  |
| partitions | [Partitions](#flyteidl-core-Partitions) |  | Think of a partition as a tag on an Artifact, except it's a key-value pair. Different partitions naturally have different versions (execution ids). |
| time_partition | [TimePartition](#flyteidl-core-TimePartition) |  | There is no such thing as an empty time partition - if it's not set, then there is no time partition. |







### ArtifactKey {#flyteidl-core-ArtifactKey}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Project and domain and suffix needs to be unique across a given artifact store. |
| domain | string |  |  |
| name | string |  |  |
| org | string |  |  |







### ArtifactQuery {#flyteidl-core-ArtifactQuery}
Uniqueness constraints for Artifacts
 - project, domain, name, version, partitions
Option 2 (tags are standalone, point to an individual artifact id):
 - project, domain, name, alias (points to one partition if partitioned)
 - project, domain, name, partition key, partition value



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact_id | [ArtifactID](#flyteidl-core-ArtifactID) |  |  |
| artifact_tag | [ArtifactTag](#flyteidl-core-ArtifactTag) |  |  |
| uri | string |  |  |
| binding | [ArtifactBindingData](#flyteidl-core-ArtifactBindingData) |  | This is used in the trigger case, where a user specifies a value for an input that is one of the triggering artifacts, or a partition value derived from a triggering artifact. |







### ArtifactTag {#flyteidl-core-ArtifactTag}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact_key | [ArtifactKey](#flyteidl-core-ArtifactKey) |  |  |
| value | [LabelValue](#flyteidl-core-LabelValue) |  |  |







### InputBindingData {#flyteidl-core-InputBindingData}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| var | string |  |  |







### LabelValue {#flyteidl-core-LabelValue}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| static_value | string |  | The string static value is for use in the Partitions object |
| time_value | google.protobuf.Timestamp |  | The time value is for use in the TimePartition case |
| triggered_binding | [ArtifactBindingData](#flyteidl-core-ArtifactBindingData) |  |  |
| input_binding | [InputBindingData](#flyteidl-core-InputBindingData) |  |  |
| runtime_binding | [RuntimeBinding](#flyteidl-core-RuntimeBinding) |  |  |







### Partitions {#flyteidl-core-Partitions}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [Partitions.ValueEntry](#flyteidl-core-Partitions-ValueEntry) | repeated |  |







### Partitions.ValueEntry {#flyteidl-core-Partitions-ValueEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | [LabelValue](#flyteidl-core-LabelValue) |  |  |







### RuntimeBinding {#flyteidl-core-RuntimeBinding}








### TimePartition {#flyteidl-core-TimePartition}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [LabelValue](#flyteidl-core-LabelValue) |  |  |
| granularity | [Granularity](#flyteidl-core-Granularity) |  |  |







### TimeTransform {#flyteidl-core-TimeTransform}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transform | string |  |  |
| op | [Operator](#flyteidl-core-Operator) |  |  |









### Granularity {#flyteidl-core-Granularity}


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| MINUTE | 1 |  |
| HOUR | 2 |  |
| DAY | 3 | default |
| MONTH | 4 |  |




### Operator {#flyteidl-core-Operator}


| Name | Number | Description |
| ---- | ------ | ----------- |
| MINUS | 0 |  |
| PLUS | 1 |  |











## flyteidl/core/types.proto




### BlobType {#flyteidl-core-BlobType}
Defines type behavior for blob objects



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| format | string |  | Format can be a free form string understood by SDK/UI etc like csv, parquet etc |
| dimensionality | [BlobType.BlobDimensionality](#flyteidl-core-BlobType-BlobDimensionality) |  |  |







### EnumType {#flyteidl-core-EnumType}
Enables declaring enum types, with predefined string values
For len(values) >gt; 0, the first value in the ordered list is regarded as the default value. If you wish
To provide no defaults, make the first value as undefined.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | string | repeated | Predefined set of enum values. |







### Error {#flyteidl-core-Error}
Represents an error thrown from a node.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| failed_node_id | string |  | The node id that threw the error. |
| message | string |  | Error message thrown. |







### LiteralType {#flyteidl-core-LiteralType}
Defines a strong type to allow type checking between interfaces.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| simple | [SimpleType](#flyteidl-core-SimpleType) |  | A simple type that can be compared one-to-one with another. |
| schema | [SchemaType](#flyteidl-core-SchemaType) |  | A complex type that requires matching of inner fields. |
| collection_type | [LiteralType](#flyteidl-core-LiteralType) |  | Defines the type of the value of a collection. Only homogeneous collections are allowed. |
| map_value_type | [LiteralType](#flyteidl-core-LiteralType) |  | Defines the type of the value of a map type. The type of the key is always a string. |
| blob | [BlobType](#flyteidl-core-BlobType) |  | A blob might have specialized implementation details depending on associated metadata. |
| enum_type | [EnumType](#flyteidl-core-EnumType) |  | Defines an enum with pre-defined string values. |
| structured_dataset_type | [StructuredDatasetType](#flyteidl-core-StructuredDatasetType) |  | Generalized schema support |
| union_type | [UnionType](#flyteidl-core-UnionType) |  | Defines an union type with pre-defined LiteralTypes. |
| metadata | google.protobuf.Struct |  | This field contains type metadata that is descriptive of the type, but is NOT considered in type-checking. This might be used by consumers to identify special behavior or display extended information for the type. |
| annotation | [TypeAnnotation](#flyteidl-core-TypeAnnotation) |  | This field contains arbitrary data that might have special semantic meaning for the client but does not effect internal flyte behavior. |
| structure | [TypeStructure](#flyteidl-core-TypeStructure) |  | Hints to improve type matching. |







### OutputReference {#flyteidl-core-OutputReference}
A reference to an output produced by a node. The type can be retrieved -and validated- from
the underlying interface of the node.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_id | string |  | Node id must exist at the graph layer. |
| var | string |  | Variable name must refer to an output variable for the node. |
| attr_path | [PromiseAttribute](#flyteidl-core-PromiseAttribute) | repeated |  |







### PromiseAttribute {#flyteidl-core-PromiseAttribute}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| string_value | string |  |  |
| int_value | int32 |  |  |







### SchemaType {#flyteidl-core-SchemaType}
Defines schema columns and types to strongly type-validate schemas interoperability.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| columns | [SchemaType.SchemaColumn](#flyteidl-core-SchemaType-SchemaColumn) | repeated | A list of ordered columns this schema comprises of. |







### SchemaType.SchemaColumn {#flyteidl-core-SchemaType-SchemaColumn}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | A unique name -within the schema type- for the column |
| type | [SchemaType.SchemaColumn.SchemaColumnType](#flyteidl-core-SchemaType-SchemaColumn-SchemaColumnType) |  | The column type. This allows a limited set of types currently. |







### StructuredDatasetType {#flyteidl-core-StructuredDatasetType}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| columns | [StructuredDatasetType.DatasetColumn](#flyteidl-core-StructuredDatasetType-DatasetColumn) | repeated | A list of ordered columns this schema comprises of. |
| format | string |  | This is the storage format, the format of the bits at rest parquet, feather, csv, etc. For two types to be compatible, the format will need to be an exact match. |
| external_schema_type | string |  | This is a string representing the type that the bytes in external_schema_bytes are formatted in. This is an optional field that will not be used for type checking. |
| external_schema_bytes | bytes |  | The serialized bytes of a third-party schema library like Arrow. This is an optional field that will not be used for type checking. |







### StructuredDatasetType.DatasetColumn {#flyteidl-core-StructuredDatasetType-DatasetColumn}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | A unique name within the schema type for the column. |
| literal_type | [LiteralType](#flyteidl-core-LiteralType) |  | The column type. |







### TypeAnnotation {#flyteidl-core-TypeAnnotation}
TypeAnnotation encapsulates registration time information about a type. This can be used for various control-plane operations. TypeAnnotation will not be available at runtime when a task runs.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| annotations | google.protobuf.Struct |  | A arbitrary JSON payload to describe a type. |







### TypeStructure {#flyteidl-core-TypeStructure}
Hints to improve type matching
e.g. allows distinguishing output from custom type transformers
even if the underlying IDL serialization matches.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tag | string |  | Must exactly match for types to be castable |
| dataclass_type | [TypeStructure.DataclassTypeEntry](#flyteidl-core-TypeStructure-DataclassTypeEntry) | repeated | dataclass_type only exists for dataclasses. This is used to resolve the type of the fields of dataclass The key is the field name, and the value is the literal type of the field e.g. For dataclass Foo, with fields a, and a is a string Foo.a will be resolved as a literal type of string from dataclass_type |







### TypeStructure.DataclassTypeEntry {#flyteidl-core-TypeStructure-DataclassTypeEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | [LiteralType](#flyteidl-core-LiteralType) |  |  |







### UnionType {#flyteidl-core-UnionType}
Defines a tagged union type, also known as a variant (and formally as the sum type).

A sum type S is defined by a sequence of types (A, B, C, ...), each tagged by a string tag
A value of type S is constructed from a value of any of the variant types. The specific choice of type is recorded by
storing the varaint's tag with the literal value and can be examined in runtime.

Type S is typically written as
S := Apple A | Banana B | Cantaloupe C | ...

Notably, a nullable (optional) type is a sum type between some type X and the singleton type representing a null-value:
Optional X := X | Null

See also: https://en.wikipedia.org/wiki/Tagged_union



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| variants | [LiteralType](#flyteidl-core-LiteralType) | repeated | Predefined set of variants in union. |









### BlobType.BlobDimensionality {#flyteidl-core-BlobType-BlobDimensionality}


| Name | Number | Description |
| ---- | ------ | ----------- |
| SINGLE | 0 |  |
| MULTIPART | 1 |  |




### SchemaType.SchemaColumn.SchemaColumnType {#flyteidl-core-SchemaType-SchemaColumn-SchemaColumnType}


| Name | Number | Description |
| ---- | ------ | ----------- |
| INTEGER | 0 |  |
| FLOAT | 1 |  |
| STRING | 2 |  |
| BOOLEAN | 3 |  |
| DATETIME | 4 |  |
| DURATION | 5 |  |




### SimpleType {#flyteidl-core-SimpleType}
Define a set of simple types.

| Name | Number | Description |
| ---- | ------ | ----------- |
| NONE | 0 |  |
| INTEGER | 1 |  |
| FLOAT | 2 |  |
| STRING | 3 |  |
| BOOLEAN | 4 |  |
| DATETIME | 5 |  |
| DURATION | 6 |  |
| BINARY | 7 |  |
| ERROR | 8 |  |
| STRUCT | 9 |  |











## flyteidl/core/execution_envs.proto




### ExecutionEnv {#flyteidl-core-ExecutionEnv}
ExecutionEnv is a message that is used to specify the execution environment.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | name is a human-readable identifier for the execution environment. This is combined with the project, domain, and version to uniquely identify an execution environment. |
| type | string |  | type is the type of the execution environment. |
| extant | google.protobuf.Struct |  | extant is a reference to an existing environment. |
| spec | google.protobuf.Struct |  | spec is a specification of the environment. |
| version | string |  | version is the version of the execution environment. This may be used differently by each individual environment type (ex. auto-generated or manually provided), but is intended to allow variance in environment specifications with the same ID. |







### ExecutionEnvAssignment {#flyteidl-core-ExecutionEnvAssignment}
ExecutionEnvAssignment is a message that is used to assign an execution environment to a set of
nodes.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_ids | string | repeated | node_ids is a list of node ids that are being assigned the execution environment. |
| task_type | string |  | task_type is the type of task that is being assigned. This is used to override which Flyte plugin will be used during execution. |
| execution_env | [ExecutionEnv](#flyteidl-core-ExecutionEnv) |  | execution_env is the environment that is being assigned to the nodes. |
















## flyteidl/core/execution.proto




### ExecutionError {#flyteidl-core-ExecutionError}
Represents the error message from the execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | string |  | Error code indicates a grouping of a type of error. More Info: <lt;Link>gt; |
| message | string |  | Detailed description of the error - including stack trace. |
| error_uri | string |  | Full error contents accessible via a URI |
| kind | [ExecutionError.ErrorKind](#flyteidl-core-ExecutionError-ErrorKind) |  |  |
| timestamp | google.protobuf.Timestamp |  | Timestamp of the error |
| worker | string |  | Worker that generated the error |







### NodeExecution {#flyteidl-core-NodeExecution}
Indicates various phases of Node Execution that only include the time spent to run the nodes/workflows







### QualityOfService {#flyteidl-core-QualityOfService}
Indicates the priority of an execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tier | [QualityOfService.Tier](#flyteidl-core-QualityOfService-Tier) |  |  |
| spec | [QualityOfServiceSpec](#flyteidl-core-QualityOfServiceSpec) |  |  |







### QualityOfServiceSpec {#flyteidl-core-QualityOfServiceSpec}
Represents customized execution run-time attributes.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| queueing_budget | google.protobuf.Duration |  | Indicates how much queueing delay an execution can tolerate. |







### TaskExecution {#flyteidl-core-TaskExecution}
Phases that task plugins can go through. Not all phases may be applicable to a specific plugin task,
but this is the cumulative list that customers may want to know about for their task.







### TaskLog {#flyteidl-core-TaskLog}
Log information for the task that is specific to a log sink
When our log story is flushed out, we may have more metadata here like log link expiry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uri | string |  |  |
| name | string |  |  |
| message_format | [TaskLog.MessageFormat](#flyteidl-core-TaskLog-MessageFormat) |  |  |
| ttl | google.protobuf.Duration |  |  |
| ShowWhilePending | bool |  |  |
| HideOnceFinished | bool |  |  |







### WorkflowExecution {#flyteidl-core-WorkflowExecution}
Indicates various phases of Workflow Execution









### ExecutionError.ErrorKind {#flyteidl-core-ExecutionError-ErrorKind}
Error type: System or User

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| USER | 1 |  |
| SYSTEM | 2 |  |




### NodeExecution.Phase {#flyteidl-core-NodeExecution-Phase}


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED | 0 |  |
| QUEUED | 1 |  |
| RUNNING | 2 |  |
| SUCCEEDED | 3 |  |
| FAILING | 4 |  |
| FAILED | 5 |  |
| ABORTED | 6 |  |
| SKIPPED | 7 |  |
| TIMED_OUT | 8 |  |
| DYNAMIC_RUNNING | 9 |  |
| RECOVERED | 10 |  |




### QualityOfService.Tier {#flyteidl-core-QualityOfService-Tier}


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED | 0 | Default: no quality of service specified. |
| HIGH | 1 |  |
| MEDIUM | 2 |  |
| LOW | 3 |  |




### TaskExecution.Phase {#flyteidl-core-TaskExecution-Phase}


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED | 0 |  |
| QUEUED | 1 |  |
| RUNNING | 2 |  |
| SUCCEEDED | 3 |  |
| ABORTED | 4 |  |
| FAILED | 5 |  |
| INITIALIZING | 6 | To indicate cases where task is initializing, like: ErrImagePull, ContainerCreating, PodInitializing |
| WAITING_FOR_RESOURCES | 7 | To address cases, where underlying resource is not available: Backoff error, Resource quota exceeded |




### TaskLog.MessageFormat {#flyteidl-core-TaskLog-MessageFormat}


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| CSV | 1 |  |
| JSON | 2 |  |




### WorkflowExecution.Phase {#flyteidl-core-WorkflowExecution-Phase}


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED | 0 |  |
| QUEUED | 1 |  |
| RUNNING | 2 |  |
| SUCCEEDING | 3 |  |
| SUCCEEDED | 4 |  |
| FAILING | 5 |  |
| FAILED | 6 |  |
| ABORTED | 7 |  |
| TIMED_OUT | 8 |  |
| ABORTING | 9 |  |











## flyteidl/core/security.proto




### Identity {#flyteidl-core-Identity}
Identity encapsulates the various security identities a task can run as. It's up to the underlying plugin to pick the
right identity for the execution environment.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| iam_role | string |  | iam_role references the fully qualified name of Identity & Access Management role to impersonate. |
| k8s_service_account | string |  | k8s_service_account references a kubernetes service account to impersonate. |
| oauth2_client | [OAuth2Client](#flyteidl-core-OAuth2Client) |  | oauth2_client references an oauth2 client. Backend plugins can use this information to impersonate the client when making external calls. |
| execution_identity | string |  | execution_identity references the subject who makes the execution |







### OAuth2Client {#flyteidl-core-OAuth2Client}
OAuth2Client encapsulates OAuth2 Client Credentials to be used when making calls on behalf of that task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| client_id | string |  | client_id is the public id for the client to use. The system will not perform any pre-auth validation that the secret requested matches the client_id indicated here. +required |
| client_secret | [Secret](#flyteidl-core-Secret) |  | client_secret is a reference to the secret used to authenticate the OAuth2 client. +required |







### OAuth2TokenRequest {#flyteidl-core-OAuth2TokenRequest}
OAuth2TokenRequest encapsulates information needed to request an OAuth2 token.
FLYTE_TOKENS_ENV_PREFIX will be passed to indicate the prefix of the environment variables that will be present if
tokens are passed through environment variables.
FLYTE_TOKENS_PATH_PREFIX will be passed to indicate the prefix of the path where secrets will be mounted if tokens
are passed through file mounts.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | name indicates a unique id for the token request within this task token requests. It'll be used as a suffix for environment variables and as a filename for mounting tokens as files. +required |
| type | [OAuth2TokenRequest.Type](#flyteidl-core-OAuth2TokenRequest-Type) |  | type indicates the type of the request to make. Defaults to CLIENT_CREDENTIALS. +required |
| client | [OAuth2Client](#flyteidl-core-OAuth2Client) |  | client references the client_id/secret to use to request the OAuth2 token. +required |
| idp_discovery_endpoint | string |  | idp_discovery_endpoint references the discovery endpoint used to retrieve token endpoint and other related information. +optional |
| token_endpoint | string |  | token_endpoint references the token issuance endpoint. If idp_discovery_endpoint is not provided, this parameter is mandatory. +optional |







### Secret {#flyteidl-core-Secret}
Secret encapsulates information about the secret a task needs to proceed. An environment variable
FLYTE_SECRETS_ENV_PREFIX will be passed to indicate the prefix of the environment variables that will be present if
secrets are passed through environment variables.
FLYTE_SECRETS_DEFAULT_DIR will be passed to indicate the prefix of the path where secrets will be mounted if secrets
are passed through file mounts.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group | string |  | The name of the secret group where to find the key referenced below. For K8s secrets, this should be the name of the v1/secret object. For Confidant, this should be the Credential name. For Vault, this should be the secret name. For AWS Secret Manager, this should be the name of the secret. +required |
| group_version | string |  | The group version to fetch. This is not supported in all secret management systems. It'll be ignored for the ones that do not support it. +optional |
| key | string |  | The name of the secret to mount. This has to match an existing secret in the system. It's up to the implementation of the secret management system to require case sensitivity. For K8s secrets, Confidant and Vault, this should match one of the keys inside the secret. For AWS Secret Manager, it's ignored. +optional |
| mount_requirement | [Secret.MountType](#flyteidl-core-Secret-MountType) |  | mount_requirement is optional. Indicates where the secret has to be mounted. If provided, the execution will fail if the underlying key management system cannot satisfy that requirement. If not provided, the default location will depend on the key management system. +optional |
| env_var | string |  | env_var is optional. Custom environment variable to set the value of the secret. If mount_requirement is ENV_VAR, then the value is the secret itself. If mount_requirement is FILE, then the value is the path to the secret file. +optional |







### SecurityContext {#flyteidl-core-SecurityContext}
SecurityContext holds security attributes that apply to tasks.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| run_as | [Identity](#flyteidl-core-Identity) |  | run_as encapsulates the identity a pod should run as. If the task fills in multiple fields here, it'll be up to the backend plugin to choose the appropriate identity for the execution engine the task will run on. |
| secrets | [Secret](#flyteidl-core-Secret) | repeated | secrets indicate the list of secrets the task needs in order to proceed. Secrets will be mounted/passed to the pod as it starts. If the plugin responsible for kicking of the task will not run it on a flyte cluster (e.g. AWS Batch), it's the responsibility of the plugin to fetch the secret (which means propeller identity will need access to the secret) and to pass it to the remote execution engine. |
| tokens | [OAuth2TokenRequest](#flyteidl-core-OAuth2TokenRequest) | repeated | tokens indicate the list of token requests the task needs in order to proceed. Tokens will be mounted/passed to the pod as it starts. If the plugin responsible for kicking of the task will not run it on a flyte cluster (e.g. AWS Batch), it's the responsibility of the plugin to fetch the secret (which means propeller identity will need access to the secret) and to pass it to the remote execution engine. |









### OAuth2TokenRequest.Type {#flyteidl-core-OAuth2TokenRequest-Type}
Type of the token requested.

| Name | Number | Description |
| ---- | ------ | ----------- |
| CLIENT_CREDENTIALS | 0 | CLIENT_CREDENTIALS indicates a 2-legged OAuth token requested using client credentials. |




### Secret.MountType {#flyteidl-core-Secret-MountType}


| Name | Number | Description |
| ---- | ------ | ----------- |
| ANY | 0 | Default case, indicates the client can tolerate either mounting options. |
| ENV_VAR | 1 | ENV_VAR indicates the secret needs to be mounted as an environment variable. |
| FILE | 2 | FILE indicates the secret needs to be mounted as a file. |











## flyteidl/core/workflow.proto




### Alias {#flyteidl-core-Alias}
Links a variable to an alias.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| var | string |  | Must match one of the output variable names on a node. |
| alias | string |  | A workflow-level unique alias that downstream nodes can refer to in their input. |







### ApproveCondition {#flyteidl-core-ApproveCondition}
ApproveCondition represents a dependency on an external approval. During execution, this will manifest as a boolean
signal with the provided signal_id.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signal_id | string |  | A unique identifier for the requested boolean signal. |







### ArrayNode {#flyteidl-core-ArrayNode}
ArrayNode is a Flyte node type that simplifies the execution of a sub-node over a list of input
values. An ArrayNode can be executed with configurable parallelism (separate from the parent
workflow) and can be configured to succeed when a certain number of sub-nodes succeed.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node | [Node](#flyteidl-core-Node) |  | node is the sub-node that will be executed for each element in the array. |
| parallelism | uint32 |  | parallelism defines the minimum number of instances to bring up concurrently at any given point. Note that this is an optimistic restriction and that, due to network partitioning or other failures, the actual number of currently running instances might be more. This has to be a positive number if assigned. Default value is size. |
| min_successes | uint32 |  | min_successes is an absolute number of the minimum number of successful completions of sub-nodes. As soon as this criteria is met, the ArrayNode will be marked as successful and outputs will be computed. This has to be a non-negative number if assigned. Default value is size (if specified). |
| min_success_ratio | float |  | If the array job size is not known beforehand, the min_success_ratio can instead be used to determine when an ArrayNode can be marked successful. |
| execution_mode | [ArrayNode.ExecutionMode](#flyteidl-core-ArrayNode-ExecutionMode) |  | execution_mode determines the execution path for ArrayNode. |
| is_original_sub_node_interface | google.protobuf.BoolValue |  | Indicates whether the sub node's original interface was altered |
| data_mode | [ArrayNode.DataMode](#flyteidl-core-ArrayNode-DataMode) |  | data_mode determines how input data is passed to the sub-nodes |
| bound_inputs | string | repeated | +optional. Specifies input bindings that are not mapped over for the node. |







### BranchNode {#flyteidl-core-BranchNode}
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| if_else | [IfElseBlock](#flyteidl-core-IfElseBlock) |  | +required |







### GateNode {#flyteidl-core-GateNode}
GateNode refers to the condition that is required for the gate to successfully complete.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| approve | [ApproveCondition](#flyteidl-core-ApproveCondition) |  | ApproveCondition represents a dependency on an external approval provided by a boolean signal. |
| signal | [SignalCondition](#flyteidl-core-SignalCondition) |  | SignalCondition represents a dependency on an signal. |
| sleep | [SleepCondition](#flyteidl-core-SleepCondition) |  | SleepCondition represents a dependency on waiting for the specified duration. |







### IfBlock {#flyteidl-core-IfBlock}
Defines a condition and the execution unit that should be executed if the condition is satisfied.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| condition | [BooleanExpression](#flyteidl-core-BooleanExpression) |  |  |
| then_node | [Node](#flyteidl-core-Node) |  |  |







### IfElseBlock {#flyteidl-core-IfElseBlock}
Defines a series of if/else blocks. The first branch whose condition evaluates to true is the one to execute.
If no conditions were satisfied, the else_node or the error will execute.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| case | [IfBlock](#flyteidl-core-IfBlock) |  | +required. First condition to evaluate. |
| other | [IfBlock](#flyteidl-core-IfBlock) | repeated | +optional. Additional branches to evaluate. |
| else_node | [Node](#flyteidl-core-Node) |  | The node to execute in case none of the branches were taken. |
| error | [Error](#flyteidl-core-Error) |  | An error to throw in case none of the branches were taken. |







### LaunchPlanTemplate {#flyteidl-core-LaunchPlanTemplate}
A structure that uniquely identifies a launch plan in the system.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [Identifier](#flyteidl-core-Identifier) |  | A globally unique identifier for the launch plan. |
| interface | [TypedInterface](#flyteidl-core-TypedInterface) |  | The input and output interface for the launch plan |
| fixed_inputs | [LiteralMap](#flyteidl-core-LiteralMap) |  | A collection of input literals that are fixed for the launch plan |







### Node {#flyteidl-core-Node}
A Workflow graph Node. One unit of execution in the graph. Each node can be linked to a Task, a Workflow or a branch
node.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | string |  | A workflow-level unique identifier that identifies this node in the workflow. 'inputs' and 'outputs' are reserved node ids that cannot be used by other nodes. |
| metadata | [NodeMetadata](#flyteidl-core-NodeMetadata) |  | Extra metadata about the node. |
| inputs | [Binding](#flyteidl-core-Binding) | repeated | Specifies how to bind the underlying interface's inputs. All required inputs specified in the underlying interface must be fulfilled. |
| upstream_node_ids | string | repeated | +optional Specifies execution dependency for this node ensuring it will only get scheduled to run after all its upstream nodes have completed. This node will have an implicit dependency on any node that appears in inputs field. |
| output_aliases | [Alias](#flyteidl-core-Alias) | repeated | +optional. A node can define aliases for a subset of its outputs. This is particularly useful if different nodes need to conform to the same interface (e.g. all branches in a branch node). Downstream nodes must refer to this nodes outputs using the alias if one's specified. |
| task_node | [TaskNode](#flyteidl-core-TaskNode) |  | Information about the Task to execute in this node. |
| workflow_node | [WorkflowNode](#flyteidl-core-WorkflowNode) |  | Information about the Workflow to execute in this mode. |
| branch_node | [BranchNode](#flyteidl-core-BranchNode) |  | Information about the branch node to evaluate in this node. |
| gate_node | [GateNode](#flyteidl-core-GateNode) |  | Information about the condition to evaluate in this node. |
| array_node | [ArrayNode](#flyteidl-core-ArrayNode) |  | Information about the sub-node executions for each value in the list of this nodes inputs values. |







### NodeMetadata {#flyteidl-core-NodeMetadata}
Defines extra information about the Node.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | A friendly name for the Node |
| timeout | google.protobuf.Duration |  | The overall timeout of a task. |
| retries | [RetryStrategy](#flyteidl-core-RetryStrategy) |  | Number of retries per task. |
| interruptible | bool |  |  |
| cacheable | bool |  |  |
| cache_version | string |  |  |
| cache_serializable | bool |  |  |
| config | [NodeMetadata.ConfigEntry](#flyteidl-core-NodeMetadata-ConfigEntry) | repeated | Config is a bag of properties that can be used to instruct propeller on how to execute the node. |







### NodeMetadata.ConfigEntry {#flyteidl-core-NodeMetadata-ConfigEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### SignalCondition {#flyteidl-core-SignalCondition}
SignalCondition represents a dependency on an signal.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signal_id | string |  | A unique identifier for the requested signal. |
| type | [LiteralType](#flyteidl-core-LiteralType) |  | A type denoting the required value type for this signal. |
| output_variable_name | string |  | The variable name for the signal value in this nodes outputs. |







### SleepCondition {#flyteidl-core-SleepCondition}
SleepCondition represents a dependency on waiting for the specified duration.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| duration | google.protobuf.Duration |  | The overall duration for this sleep. |







### TaskNode {#flyteidl-core-TaskNode}
Refers to the task that the Node is to execute.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reference_id | [Identifier](#flyteidl-core-Identifier) |  | A globally unique identifier for the task. |
| overrides | [TaskNodeOverrides](#flyteidl-core-TaskNodeOverrides) |  | Optional overrides applied at task execution time. |







### TaskNodeOverrides {#flyteidl-core-TaskNodeOverrides}
Optional task node overrides that will be applied at task execution time.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resources | [Resources](#flyteidl-core-Resources) |  | A customizable interface to convey resources requested for a task container. |
| extended_resources | [ExtendedResources](#flyteidl-core-ExtendedResources) |  | Overrides for all non-standard resources, not captured by v1.ResourceRequirements, to allocate to a task. |
| container_image | string |  | Override for the image used by task pods. |
| pod_template | [K8sPod](#flyteidl-core-K8sPod) |  | Override for the pod template used by task pods +optional |







### WorkflowMetadata {#flyteidl-core-WorkflowMetadata}
This is workflow layer metadata. These settings are only applicable to the workflow as a whole, and do not
percolate down to child entities (like tasks) launched by the workflow.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| quality_of_service | [QualityOfService](#flyteidl-core-QualityOfService) |  | Indicates the runtime priority of workflow executions. |
| on_failure | [WorkflowMetadata.OnFailurePolicy](#flyteidl-core-WorkflowMetadata-OnFailurePolicy) |  | Defines how the system should behave when a failure is detected in the workflow execution. |
| tags | [WorkflowMetadata.TagsEntry](#flyteidl-core-WorkflowMetadata-TagsEntry) | repeated | Arbitrary tags that allow users and the platform to store small but arbitrary labels |







### WorkflowMetadata.TagsEntry {#flyteidl-core-WorkflowMetadata-TagsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### WorkflowMetadataDefaults {#flyteidl-core-WorkflowMetadataDefaults}
The difference between these settings and the WorkflowMetadata ones is that these are meant to be passed down to
a workflow's underlying entities (like tasks). For instance, 'interruptible' has no meaning at the workflow layer, it
is only relevant when a task executes. The settings here are the defaults that are passed to all nodes
unless explicitly overridden at the node layer.
If you are adding a setting that applies to both the Workflow itself, and everything underneath it, it should be
added to both this object and the WorkflowMetadata object above.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| interruptible | bool |  | Whether child nodes of the workflow are interruptible. |







### WorkflowNode {#flyteidl-core-WorkflowNode}
Refers to a the workflow the node is to execute.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| launchplan_ref | [Identifier](#flyteidl-core-Identifier) |  | A globally unique identifier for the launch plan. |
| sub_workflow_ref | [Identifier](#flyteidl-core-Identifier) |  | Reference to a subworkflow, that should be defined with the compiler context |







### WorkflowTemplate {#flyteidl-core-WorkflowTemplate}
Flyte Workflow Structure that encapsulates task, branch and subworkflow nodes to form a statically analyzable,
directed acyclic graph.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [Identifier](#flyteidl-core-Identifier) |  | A globally unique identifier for the workflow. |
| metadata | [WorkflowMetadata](#flyteidl-core-WorkflowMetadata) |  | Extra metadata about the workflow. |
| interface | [TypedInterface](#flyteidl-core-TypedInterface) |  | Defines a strongly typed interface for the Workflow. This can include some optional parameters. |
| nodes | [Node](#flyteidl-core-Node) | repeated | A list of nodes. In addition, 'globals' is a special reserved node id that can be used to consume workflow inputs. |
| outputs | [Binding](#flyteidl-core-Binding) | repeated | A list of output bindings that specify how to construct workflow outputs. Bindings can pull node outputs or specify literals. All workflow outputs specified in the interface field must be bound in order for the workflow to be validated. A workflow has an implicit dependency on all of its nodes to execute successfully in order to bind final outputs. Most of these outputs will be Binding's with a BindingData of type OutputReference. That is, your workflow can just have an output of some constant (`Output(5)`), but usually, the workflow will be pulling outputs from the output of a task. |
| failure_node | [Node](#flyteidl-core-Node) |  | +optional A catch-all node. This node is executed whenever the execution engine determines the workflow has failed. The interface of this node must match the Workflow interface with an additional input named 'error' of type pb.lyft.flyte.core.Error. |
| metadata_defaults | [WorkflowMetadataDefaults](#flyteidl-core-WorkflowMetadataDefaults) |  | workflow defaults |









### ArrayNode.DataMode {#flyteidl-core-ArrayNode-DataMode}


| Name | Number | Description |
| ---- | ------ | ----------- |
| SINGLE_INPUT_FILE | 0 | Indicates the ArrayNode's input is a list of input values that map to subNode executions. The file path set for the subNode will be the ArrayNode's input file, but the in-memory value utilized in propeller will be the individual value for each subNode execution. SubNode executions need to be able to read in and parse the individual value to execute correctly. |
| INDIVIDUAL_INPUT_FILES | 1 | Indicates the ArrayNode's input is a list of input values that map to subNode executions. Propeller will create input files for each ArrayNode subNode by parsing the inputs and setting the InputBindings on each subNodeSpec. Both the file path and in-memory input values will be the individual value for each subNode execution. |




### ArrayNode.ExecutionMode {#flyteidl-core-ArrayNode-ExecutionMode}


| Name | Number | Description |
| ---- | ------ | ----------- |
| MINIMAL_STATE | 0 | Indicates the ArrayNode will store minimal state for the sub-nodes. This is more efficient, but only supports a subset of Flyte entities. |
| FULL_STATE | 1 | Indicates the ArrayNode will store full state for the sub-nodes. This supports a wider range of Flyte entities. |




### WorkflowMetadata.OnFailurePolicy {#flyteidl-core-WorkflowMetadata-OnFailurePolicy}
Failure Handling Strategy

| Name | Number | Description |
| ---- | ------ | ----------- |
| FAIL_IMMEDIATELY | 0 | FAIL_IMMEDIATELY instructs the system to fail as soon as a node fails in the workflow. It'll automatically abort all currently running nodes and clean up resources before finally marking the workflow executions as failed. |
| FAIL_AFTER_EXECUTABLE_NODES_COMPLETE | 1 | FAIL_AFTER_EXECUTABLE_NODES_COMPLETE instructs the system to make as much progress as it can. The system will not alter the dependencies of the execution graph so any node that depend on the failed node will not be run. Other nodes that will be executed to completion before cleaning up resources and marking the workflow execution as failed. |











## flyteidl/core/workflow_closure.proto




### WorkflowClosure {#flyteidl-core-WorkflowClosure}
Defines an enclosed package of workflow and tasks it references.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| workflow | [WorkflowTemplate](#flyteidl-core-WorkflowTemplate) |  | required. Workflow template. |
| tasks | [TaskTemplate](#flyteidl-core-TaskTemplate) | repeated | optional. A collection of tasks referenced by the workflow. Only needed if the workflow references tasks. |
















## flyteidl/core/condition.proto




### BooleanExpression {#flyteidl-core-BooleanExpression}
Defines a boolean expression tree. It can be a simple or a conjunction expression.
Multiple expressions can be combined using a conjunction or a disjunction to result in a final boolean result.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| conjunction | [ConjunctionExpression](#flyteidl-core-ConjunctionExpression) |  |  |
| comparison | [ComparisonExpression](#flyteidl-core-ComparisonExpression) |  |  |







### ComparisonExpression {#flyteidl-core-ComparisonExpression}
Defines a 2-level tree where the root is a comparison operator and Operands are primitives or known variables.
Each expression results in a boolean result.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| operator | [ComparisonExpression.Operator](#flyteidl-core-ComparisonExpression-Operator) |  |  |
| left_value | [Operand](#flyteidl-core-Operand) |  |  |
| right_value | [Operand](#flyteidl-core-Operand) |  |  |







### ConjunctionExpression {#flyteidl-core-ConjunctionExpression}
Defines a conjunction expression of two boolean expressions.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| operator | [ConjunctionExpression.LogicalOperator](#flyteidl-core-ConjunctionExpression-LogicalOperator) |  |  |
| left_expression | [BooleanExpression](#flyteidl-core-BooleanExpression) |  |  |
| right_expression | [BooleanExpression](#flyteidl-core-BooleanExpression) |  |  |







### Operand {#flyteidl-core-Operand}
Defines an operand to a comparison expression.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| primitive | [Primitive](#flyteidl-core-Primitive) |  | **Deprecated.** Can be a constant |
| var | string |  | Or one of this node's input variables |
| scalar | [Scalar](#flyteidl-core-Scalar) |  | Replace the primitive field |









### ComparisonExpression.Operator {#flyteidl-core-ComparisonExpression-Operator}
Binary Operator for each expression

| Name | Number | Description |
| ---- | ------ | ----------- |
| EQ | 0 |  |
| NEQ | 1 |  |
| GT | 2 | Greater Than |
| GTE | 3 |  |
| LT | 4 | Less Than |
| LTE | 5 |  |




### ConjunctionExpression.LogicalOperator {#flyteidl-core-ConjunctionExpression-LogicalOperator}
Nested conditions. They can be conjoined using AND / OR
Order of evaluation is not important as the operators are Commutative

| Name | Number | Description |
| ---- | ------ | ----------- |
| AND | 0 | Conjunction |
| OR | 1 |  |











## flyteidl/core/dynamic_job.proto




### DynamicJobSpec {#flyteidl-core-DynamicJobSpec}
Describes a set of tasks to execute and how the final outputs are produced.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| nodes | [Node](#flyteidl-core-Node) | repeated | A collection of nodes to execute. |
| min_successes | int64 |  | An absolute number of successful completions of nodes required to mark this job as succeeded. As soon as this criteria is met, the dynamic job will be marked as successful and outputs will be computed. If this number becomes impossible to reach (e.g. number of currently running tasks + number of already succeeded tasks <lt; min_successes) the task will be aborted immediately and marked as failed. The default value of this field, if not specified, is the count of nodes repeated field. |
| outputs | [Binding](#flyteidl-core-Binding) | repeated | Describes how to bind the final output of the dynamic job from the outputs of executed nodes. The referenced ids in bindings should have the generated id for the subtask. |
| tasks | [TaskTemplate](#flyteidl-core-TaskTemplate) | repeated | [Optional] A complete list of task specs referenced in nodes. |
| subworkflows | [WorkflowTemplate](#flyteidl-core-WorkflowTemplate) | repeated | [Optional] A complete list of task specs referenced in nodes. |
















## flyteidl/plugins/presto.proto




### PrestoQuery {#flyteidl-plugins-PrestoQuery}
This message works with the 'presto' task type in the SDK and is the object that will be in the 'custom' field
of a Presto task's TaskTemplate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| routing_group | string |  |  |
| catalog | string |  |  |
| schema | string |  |  |
| statement | string |  |  |
















## flyteidl/plugins/qubole.proto




### HiveQuery {#flyteidl-plugins-HiveQuery}
Defines a query to execute on a hive cluster.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | string |  |  |
| timeout_sec | uint32 |  |  |
| retryCount | uint32 |  |  |







### HiveQueryCollection {#flyteidl-plugins-HiveQueryCollection}
Defines a collection of hive queries.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| queries | [HiveQuery](#flyteidl-plugins-HiveQuery) | repeated |  |







### QuboleHiveJob {#flyteidl-plugins-QuboleHiveJob}
This message works with the 'hive' task type in the SDK and is the object that will be in the 'custom' field
of a hive task's TaskTemplate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cluster_label | string |  |  |
| query_collection | [HiveQueryCollection](#flyteidl-plugins-HiveQueryCollection) |  | **Deprecated.**  |
| tags | string | repeated |  |
| query | [HiveQuery](#flyteidl-plugins-HiveQuery) |  |  |
















## flyteidl/plugins/ray.proto




### HeadGroupSpec {#flyteidl-plugins-HeadGroupSpec}
HeadGroupSpec are the spec for the head pod



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ray_start_params | [HeadGroupSpec.RayStartParamsEntry](#flyteidl-plugins-HeadGroupSpec-RayStartParamsEntry) | repeated | Optional. RayStartParams are the params of the start command: address, object-store-memory. Refer to https://docs.ray.io/en/latest/ray-core/package-ref.html#ray-start |
| k8s_pod | [flyteidl.core.K8sPod](#flyteidl-core-K8sPod) |  | Pod Spec for the ray head pod |







### HeadGroupSpec.RayStartParamsEntry {#flyteidl-plugins-HeadGroupSpec-RayStartParamsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### RayCluster {#flyteidl-plugins-RayCluster}
Define Ray cluster defines the desired state of RayCluster



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| head_group_spec | [HeadGroupSpec](#flyteidl-plugins-HeadGroupSpec) |  | HeadGroupSpecs are the spec for the head pod |
| worker_group_spec | [WorkerGroupSpec](#flyteidl-plugins-WorkerGroupSpec) | repeated | WorkerGroupSpecs are the specs for the worker pods |
| enable_autoscaling | bool |  | Whether to enable autoscaling. |







### RayJob {#flyteidl-plugins-RayJob}
RayJobSpec defines the desired state of RayJob



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ray_cluster | [RayCluster](#flyteidl-plugins-RayCluster) |  | RayClusterSpec is the cluster template to run the job |
| runtime_env | string |  | **Deprecated.** runtime_env is base64 encoded. Ray runtime environments: https://docs.ray.io/en/latest/ray-core/handling-dependencies.html#runtime-environments |
| shutdown_after_job_finishes | bool |  | shutdown_after_job_finishes specifies whether the RayCluster should be deleted after the RayJob finishes. |
| ttl_seconds_after_finished | int32 |  | ttl_seconds_after_finished specifies the number of seconds after which the RayCluster will be deleted after the RayJob finishes. |
| runtime_env_yaml | string |  | RuntimeEnvYAML represents the runtime environment configuration provided as a multi-line YAML string. |







### WorkerGroupSpec {#flyteidl-plugins-WorkerGroupSpec}
WorkerGroupSpec are the specs for the worker pods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_name | string |  | Required. RayCluster can have multiple worker groups, and it distinguishes them by name |
| replicas | int32 |  | Required. Desired replicas of the worker group. Defaults to 1. |
| min_replicas | int32 |  | Optional. Min replicas of the worker group. MinReplicas defaults to 1. |
| max_replicas | int32 |  | Optional. Max replicas of the worker group. MaxReplicas defaults to maxInt32 |
| ray_start_params | [WorkerGroupSpec.RayStartParamsEntry](#flyteidl-plugins-WorkerGroupSpec-RayStartParamsEntry) | repeated | Optional. RayStartParams are the params of the start command: address, object-store-memory. Refer to https://docs.ray.io/en/latest/ray-core/package-ref.html#ray-start |
| k8s_pod | [flyteidl.core.K8sPod](#flyteidl-core-K8sPod) |  | Pod Spec for ray worker pods |







### WorkerGroupSpec.RayStartParamsEntry {#flyteidl-plugins-WorkerGroupSpec-RayStartParamsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |
















## flyteidl/plugins/spark.proto




### SparkApplication {#flyteidl-plugins-SparkApplication}








### SparkJob {#flyteidl-plugins-SparkJob}
Custom Proto for Spark Plugin.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| applicationType | [SparkApplication.Type](#flyteidl-plugins-SparkApplication-Type) |  |  |
| mainApplicationFile | string |  |  |
| mainClass | string |  |  |
| sparkConf | [SparkJob.SparkConfEntry](#flyteidl-plugins-SparkJob-SparkConfEntry) | repeated |  |
| hadoopConf | [SparkJob.HadoopConfEntry](#flyteidl-plugins-SparkJob-HadoopConfEntry) | repeated |  |
| executorPath | string |  | Executor path for Python jobs. |
| databricksConf | google.protobuf.Struct |  | Databricks job configuration. Config structure can be found here. https://docs.databricks.com/dev-tools/api/2.0/jobs.html#request-structure. |
| databricksToken | string |  | Databricks access token. https://docs.databricks.com/dev-tools/api/latest/authentication.html This token can be set in either flytepropeller or flytekit. |
| databricksInstance | string |  | Domain name of your deployment. Use the form <lt;account>gt;.cloud.databricks.com. This instance name can be set in either flytepropeller or flytekit. |
| driverPod | [flyteidl.core.K8sPod](#flyteidl-core-K8sPod) |  | Pod Spec for the Spark driver pod |
| executorPod | [flyteidl.core.K8sPod](#flyteidl-core-K8sPod) |  | Pod Spec for the Spark executor pod |







### SparkJob.HadoopConfEntry {#flyteidl-plugins-SparkJob-HadoopConfEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### SparkJob.SparkConfEntry {#flyteidl-plugins-SparkJob-SparkConfEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |









### SparkApplication.Type {#flyteidl-plugins-SparkApplication-Type}


| Name | Number | Description |
| ---- | ------ | ----------- |
| PYTHON | 0 |  |
| JAVA | 1 |  |
| SCALA | 2 |  |
| R | 3 |  |











## flyteidl/plugins/array_job.proto




### ArrayJob {#flyteidl-plugins-ArrayJob}
Describes a job that can process independent pieces of data concurrently. Multiple copies of the runnable component
will be executed concurrently.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| parallelism | int64 |  | Defines the maximum number of instances to bring up concurrently at any given point. Note that this is an optimistic restriction and that, due to network partitioning or other failures, the actual number of currently running instances might be more. This has to be a positive number if assigned. Default value is size. |
| size | int64 |  | Defines the number of instances to launch at most. This number should match the size of the input if the job requires processing of all input data. This has to be a positive number. In the case this is not defined, the back-end will determine the size at run-time by reading the inputs. |
| min_successes | int64 |  | An absolute number of the minimum number of successful completions of subtasks. As soon as this criteria is met, the array job will be marked as successful and outputs will be computed. This has to be a non-negative number if assigned. Default value is size (if specified). |
| min_success_ratio | float |  | If the array job size is not known beforehand, the min_success_ratio can instead be used to determine when an array job can be marked successful. |
















## flyteidl/plugins/waitable.proto




### Waitable {#flyteidl-plugins-Waitable}
Represents an Execution that was launched and could be waited on.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wf_exec_id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  |  |
| phase | [flyteidl.core.WorkflowExecution.Phase](#flyteidl-core-WorkflowExecution-Phase) |  |  |
| workflow_id | string |  |  |
















## flyteidl/plugins/dask.proto




### DaskJob {#flyteidl-plugins-DaskJob}
Custom Proto for Dask Plugin.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| scheduler | [DaskScheduler](#flyteidl-plugins-DaskScheduler) |  | Spec for the scheduler pod. |
| workers | [DaskWorkerGroup](#flyteidl-plugins-DaskWorkerGroup) |  | Spec of the default worker group. |







### DaskScheduler {#flyteidl-plugins-DaskScheduler}
Specification for the scheduler pod.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| image | string |  | Optional image to use. If unset, will use the default image. |
| resources | [flyteidl.core.Resources](#flyteidl-core-Resources) |  | Resources assigned to the scheduler pod. |







### DaskWorkerGroup {#flyteidl-plugins-DaskWorkerGroup}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| number_of_workers | uint32 |  | Number of workers in the group. |
| image | string |  | Optional image to use for the pods of the worker group. If unset, will use the default image. |
| resources | [flyteidl.core.Resources](#flyteidl-core-Resources) |  | Resources assigned to the all pods of the worker group. As per https://kubernetes.dask.org/en/latest/kubecluster.html?highlight=limit#best-practices it is advised to only set limits. If requests are not explicitly set, the plugin will make sure to set requests==limits. The plugin sets ` --memory-limit` as well as `--nthreads` for the workers according to the limit. |
















## flyteidl/plugins/mpi.proto




### DistributedMPITrainingTask {#flyteidl-plugins-DistributedMPITrainingTask}
MPI operator proposal https://github.com/kubeflow/community/blob/master/proposals/mpi-operator-proposal.md
Custom proto for plugin that enables distributed training using https://github.com/kubeflow/mpi-operator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| num_workers | int32 |  | number of worker spawned in the cluster for this job |
| num_launcher_replicas | int32 |  | number of launcher replicas spawned in the cluster for this job The launcher pod invokes mpirun and communicates with worker pods through MPI. |
| slots | int32 |  | number of slots per worker used in hostfile. The available slots (GPUs) in each pod. |
















## flyteidl/plugins/pytorch.proto




### DistributedPyTorchTrainingTask {#flyteidl-plugins-DistributedPyTorchTrainingTask}
Custom proto for plugin that enables distributed training using https://github.com/kubeflow/pytorch-operator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| workers | int32 |  | number of worker replicas spawned in the cluster for this job |
| elastic_config | [ElasticConfig](#flyteidl-plugins-ElasticConfig) |  | config for an elastic pytorch job |







### ElasticConfig {#flyteidl-plugins-ElasticConfig}
Custom proto for torch elastic config for distributed training using
https://github.com/kubeflow/training-operator/blob/master/pkg/apis/kubeflow.org/v1/pytorch_types.go



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rdzv_backend | string |  |  |
| min_replicas | int32 |  |  |
| max_replicas | int32 |  |  |
| nproc_per_node | int32 |  |  |
| max_restarts | int32 |  |  |
















## flyteidl/plugins/kubeflow/mpi.proto




### DistributedMPITrainingReplicaSpec {#flyteidl-plugins-kubeflow-DistributedMPITrainingReplicaSpec}
Replica specification for distributed MPI training



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| replicas | int32 |  | **Deprecated.** 1~4 deprecated. Use common instead. Number of replicas |
| image | string |  | **Deprecated.** Image used for the replica group |
| resources | [flyteidl.core.Resources](#flyteidl-core-Resources) |  | **Deprecated.** Resources required for the replica group |
| restart_policy | [flyteidl.plugins.RestartPolicy](#flyteidl-plugins-RestartPolicy) |  | **Deprecated.** Restart policy determines whether pods will be restarted when they exit |
| command | string | repeated | MPI sometimes requires different command set for different replica groups |
| common | [flyteidl.plugins.CommonReplicaSpec](#flyteidl-plugins-CommonReplicaSpec) |  | The common replica spec |







### DistributedMPITrainingTask {#flyteidl-plugins-kubeflow-DistributedMPITrainingTask}
Proto for plugin that enables distributed training using https://github.com/kubeflow/mpi-operator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| worker_replicas | [DistributedMPITrainingReplicaSpec](#flyteidl-plugins-kubeflow-DistributedMPITrainingReplicaSpec) |  | Worker replicas spec |
| launcher_replicas | [DistributedMPITrainingReplicaSpec](#flyteidl-plugins-kubeflow-DistributedMPITrainingReplicaSpec) |  | Master replicas spec |
| run_policy | [RunPolicy](#flyteidl-plugins-kubeflow-RunPolicy) |  | RunPolicy encapsulates various runtime policies of the distributed training job, for example how to clean up resources and how long the job can stay active. |
| slots | int32 |  | Number of slots per worker |
















## flyteidl/plugins/kubeflow/pytorch.proto




### DistributedPyTorchTrainingReplicaSpec {#flyteidl-plugins-kubeflow-DistributedPyTorchTrainingReplicaSpec}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| replicas | int32 |  | **Deprecated.** 1~4 deprecated. Use common instead. Number of replicas |
| image | string |  | **Deprecated.** Image used for the replica group |
| resources | [flyteidl.core.Resources](#flyteidl-core-Resources) |  | **Deprecated.** Resources required for the replica group |
| restart_policy | [flyteidl.plugins.RestartPolicy](#flyteidl-plugins-RestartPolicy) |  | **Deprecated.** Restart policy determines whether pods will be restarted when they exit |
| common | [flyteidl.plugins.CommonReplicaSpec](#flyteidl-plugins-CommonReplicaSpec) |  | The common replica spec |







### DistributedPyTorchTrainingTask {#flyteidl-plugins-kubeflow-DistributedPyTorchTrainingTask}
Proto for plugin that enables distributed training using https://github.com/kubeflow/pytorch-operator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| worker_replicas | [DistributedPyTorchTrainingReplicaSpec](#flyteidl-plugins-kubeflow-DistributedPyTorchTrainingReplicaSpec) |  | Worker replicas spec |
| master_replicas | [DistributedPyTorchTrainingReplicaSpec](#flyteidl-plugins-kubeflow-DistributedPyTorchTrainingReplicaSpec) |  | Master replicas spec, master replicas can only have 1 replica |
| run_policy | [RunPolicy](#flyteidl-plugins-kubeflow-RunPolicy) |  | RunPolicy encapsulates various runtime policies of the distributed training job, for example how to clean up resources and how long the job can stay active. |
| elastic_config | [ElasticConfig](#flyteidl-plugins-kubeflow-ElasticConfig) |  | config for an elastic pytorch job |







### ElasticConfig {#flyteidl-plugins-kubeflow-ElasticConfig}
Custom proto for torch elastic config for distributed training using
https://github.com/kubeflow/training-operator/blob/master/pkg/apis/kubeflow.org/v1/pytorch_types.go



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rdzv_backend | string |  |  |
| min_replicas | int32 |  |  |
| max_replicas | int32 |  |  |
| nproc_per_node | int32 |  |  |
| max_restarts | int32 |  |  |
















## flyteidl/plugins/kubeflow/tensorflow.proto




### DistributedTensorflowTrainingReplicaSpec {#flyteidl-plugins-kubeflow-DistributedTensorflowTrainingReplicaSpec}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| replicas | int32 |  | **Deprecated.** 1~4 deprecated. Use common instead. Number of replicas |
| image | string |  | **Deprecated.** Image used for the replica group |
| resources | [flyteidl.core.Resources](#flyteidl-core-Resources) |  | **Deprecated.** Resources required for the replica group |
| restart_policy | [flyteidl.plugins.RestartPolicy](#flyteidl-plugins-RestartPolicy) |  | **Deprecated.** Restart policy determines whether pods will be restarted when they exit |
| common | [flyteidl.plugins.CommonReplicaSpec](#flyteidl-plugins-CommonReplicaSpec) |  | The common replica spec |







### DistributedTensorflowTrainingTask {#flyteidl-plugins-kubeflow-DistributedTensorflowTrainingTask}
Proto for plugin that enables distributed training using https://github.com/kubeflow/tf-operator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| worker_replicas | [DistributedTensorflowTrainingReplicaSpec](#flyteidl-plugins-kubeflow-DistributedTensorflowTrainingReplicaSpec) |  | Worker replicas spec |
| ps_replicas | [DistributedTensorflowTrainingReplicaSpec](#flyteidl-plugins-kubeflow-DistributedTensorflowTrainingReplicaSpec) |  | Parameter server replicas spec |
| chief_replicas | [DistributedTensorflowTrainingReplicaSpec](#flyteidl-plugins-kubeflow-DistributedTensorflowTrainingReplicaSpec) |  | Chief replicas spec |
| run_policy | [RunPolicy](#flyteidl-plugins-kubeflow-RunPolicy) |  | RunPolicy encapsulates various runtime policies of the distributed training job, for example how to clean up resources and how long the job can stay active. |
| evaluator_replicas | [DistributedTensorflowTrainingReplicaSpec](#flyteidl-plugins-kubeflow-DistributedTensorflowTrainingReplicaSpec) |  | Evaluator replicas spec |
















## flyteidl/plugins/kubeflow/common.proto




### RunPolicy {#flyteidl-plugins-kubeflow-RunPolicy}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| clean_pod_policy | [CleanPodPolicy](#flyteidl-plugins-kubeflow-CleanPodPolicy) |  | Defines the policy to kill pods after the job completes. Default to None. |
| ttl_seconds_after_finished | int32 |  | TTL to clean up jobs. Default to infinite. |
| active_deadline_seconds | int32 |  | Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer. |
| backoff_limit | int32 |  | Number of retries before marking this job failed. |









### CleanPodPolicy {#flyteidl-plugins-kubeflow-CleanPodPolicy}


| Name | Number | Description |
| ---- | ------ | ----------- |
| CLEANPOD_POLICY_NONE | 0 |  |
| CLEANPOD_POLICY_RUNNING | 1 |  |
| CLEANPOD_POLICY_ALL | 2 |  |











## flyteidl/plugins/tensorflow.proto




### DistributedTensorflowTrainingTask {#flyteidl-plugins-DistributedTensorflowTrainingTask}
Custom proto for plugin that enables distributed training using https://github.com/kubeflow/tf-operator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| workers | int32 |  | number of worker replicas spawned in the cluster for this job |
| ps_replicas | int32 |  | PS ->gt; Parameter server number of ps replicas spawned in the cluster for this job |
| chief_replicas | int32 |  | number of chief replicas spawned in the cluster for this job |
| evaluator_replicas | int32 |  | number of evaluator replicas spawned in the cluster for this job |
















## flyteidl/plugins/common.proto




### CommonReplicaSpec {#flyteidl-plugins-CommonReplicaSpec}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| replicas | int32 |  | Number of replicas |
| image | string |  | Image used for the replica group |
| resources | [flyteidl.core.Resources](#flyteidl-core-Resources) |  | Resources required for the replica group |
| restart_policy | [RestartPolicy](#flyteidl-plugins-RestartPolicy) |  | RestartPolicy determines whether pods will be restarted when they exit |









### RestartPolicy {#flyteidl-plugins-RestartPolicy}


| Name | Number | Description |
| ---- | ------ | ----------- |
| RESTART_POLICY_NEVER | 0 |  |
| RESTART_POLICY_ON_FAILURE | 1 |  |
| RESTART_POLICY_ALWAYS | 2 |  |











## flyteidl/admin/schedule.proto




### CronSchedule {#flyteidl-admin-CronSchedule}
Options for schedules to run according to a cron expression.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| schedule | string |  | Standard/default cron implementation as described by https://en.wikipedia.org/wiki/Cron#CRON_expression; Also supports nonstandard predefined scheduling definitions as described by https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions except @reboot |
| offset | string |  | ISO 8601 duration as described by https://en.wikipedia.org/wiki/ISO_8601#Durations |







### FixedRate {#flyteidl-admin-FixedRate}
Option for schedules run at a certain frequency e.g. every 2 minutes.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | uint32 |  |  |
| unit | [FixedRateUnit](#flyteidl-admin-FixedRateUnit) |  |  |







### Schedule {#flyteidl-admin-Schedule}
Defines complete set of information required to trigger an execution on a schedule.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cron_expression | string |  | **Deprecated.** Uses AWS syntax: Minutes Hours Day-of-month Month Day-of-week Year e.g. for a schedule that runs every 15 minutes: 0/15 * * * ? * |
| rate | [FixedRate](#flyteidl-admin-FixedRate) |  |  |
| cron_schedule | [CronSchedule](#flyteidl-admin-CronSchedule) |  |  |
| kickoff_time_input_arg | string |  | Name of the input variable that the kickoff time will be supplied to when the workflow is kicked off. |









### FixedRateUnit {#flyteidl-admin-FixedRateUnit}
Represents a frequency at which to run a schedule.

| Name | Number | Description |
| ---- | ------ | ----------- |
| MINUTE | 0 |  |
| HOUR | 1 |  |
| DAY | 2 |  |











## flyteidl/admin/project.proto




### Domain {#flyteidl-admin-Domain}
Namespace within a project commonly used to differentiate between different service instances.
e.g. "production", "development", etc.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | string |  | Globally unique domain name. |
| name | string |  | Display name. |







### GetDomainRequest {#flyteidl-admin-GetDomainRequest}
Empty request for GetDomain







### GetDomainsResponse {#flyteidl-admin-GetDomainsResponse}
Represents a list of domains.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| domains | [Domain](#flyteidl-admin-Domain) | repeated |  |







### InactiveProject {#flyteidl-admin-InactiveProject}
Error returned for inactive projects



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | string |  | Indicates a unique project. +required |
| org | string |  | Optional, org key applied to the resource. |







### Project {#flyteidl-admin-Project}
Top-level namespace used to classify different entities like workflows and executions.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | string |  | Globally unique project name. |
| name | string |  | Display name. |
| domains | [Domain](#flyteidl-admin-Domain) | repeated |  |
| description | string |  |  |
| labels | [Labels](#flyteidl-admin-Labels) |  | Leverage Labels from flyteidl.admin.common.proto to tag projects with ownership information. |
| state | [Project.ProjectState](#flyteidl-admin-Project-ProjectState) |  |  |
| org | string |  | Optional, org key applied to the resource. |







### ProjectGetRequest {#flyteidl-admin-ProjectGetRequest}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | string |  | Indicates a unique project. +required |
| org | string |  | Optional, org key applied to the resource. |







### ProjectListRequest {#flyteidl-admin-ProjectListRequest}
Request to retrieve a list of projects matching specified filters.
See :ref:`ref_flyteidl.admin.Project` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| limit | uint32 |  | Indicates the number of projects to be returned. +required |
| token | string |  | In the case of multiple pages of results, this server-provided token can be used to fetch the next page in a query. +optional |
| filters | string |  | Indicates a list of filters passed as string. More info on constructing filters : <lt;Link>gt; +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Sort ordering. +optional |
| org | string |  | Optional, org filter applied to list project requests. |







### ProjectRegisterRequest {#flyteidl-admin-ProjectRegisterRequest}
Adds a new user-project within the Flyte deployment.
See :ref:`ref_flyteidl.admin.Project` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | [Project](#flyteidl-admin-Project) |  | +required |







### ProjectRegisterResponse {#flyteidl-admin-ProjectRegisterResponse}
Purposefully empty, may be updated in the future.







### ProjectUpdateResponse {#flyteidl-admin-ProjectUpdateResponse}
Purposefully empty, may be updated in the future.







### Projects {#flyteidl-admin-Projects}
Represents a list of projects.
See :ref:`ref_flyteidl.admin.Project` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| projects | [Project](#flyteidl-admin-Project) | repeated |  |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |









### Project.ProjectState {#flyteidl-admin-Project-ProjectState}
The state of the project is used to control its visibility in the UI and validity.

| Name | Number | Description |
| ---- | ------ | ----------- |
| ACTIVE | 0 | By default, all projects are considered active. |
| ARCHIVED | 1 | Archived projects are no longer visible in the UI and no longer valid. |
| SYSTEM_GENERATED | 2 | System generated projects that aren't explicitly created or managed by a user. |
| SYSTEM_ARCHIVED | 3 | System archived projects that aren't explicitly archived by a user. |











## flyteidl/admin/cluster_assignment.proto




### ClusterAssignment {#flyteidl-admin-ClusterAssignment}
Encapsulates specifications for routing an execution onto a specific cluster.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cluster_pool_name | string |  |  |
















## flyteidl/admin/notification.proto




### EmailMessage {#flyteidl-admin-EmailMessage}
Represents the Email object that is sent to a publisher/subscriber
to forward the notification.
Note: This is internal to Admin and doesn't need to be exposed to other components.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipients_email | string | repeated | The list of email addresses to receive an email with the content populated in the other fields. Currently, each email recipient will receive its own email. This populates the TO field. |
| sender_email | string |  | The email of the sender. This populates the FROM field. |
| subject_line | string |  | The content of the subject line. This populates the SUBJECT field. |
| body | string |  | The content of the email body. This populates the BODY field. |
















## flyteidl/admin/task.proto




### Task {#flyteidl-admin-Task}
Flyte workflows are composed of many ordered tasks. That is small, reusable, self-contained logical blocks
arranged to process workflow inputs and produce a deterministic set of outputs.
Tasks can come in many varieties tuned for specialized behavior.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | id represents the unique identifier of the task. |
| closure | [TaskClosure](#flyteidl-admin-TaskClosure) |  | closure encapsulates all the fields that maps to a compiled version of the task. |
| short_description | string |  | One-liner overview of the entity. |







### TaskClosure {#flyteidl-admin-TaskClosure}
Compute task attributes which include values derived from the TaskSpec, as well as plugin-specific data
and task metadata.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| compiled_task | [flyteidl.core.CompiledTask](#flyteidl-core-CompiledTask) |  | Represents the compiled representation of the task from the specification provided. |
| created_at | google.protobuf.Timestamp |  | Time at which the task was created. |







### TaskCreateRequest {#flyteidl-admin-TaskCreateRequest}
Represents a request structure to create a revision of a task.
See :ref:`ref_flyteidl.admin.Task` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | id represents the unique identifier of the task. +required |
| spec | [TaskSpec](#flyteidl-admin-TaskSpec) |  | Represents the specification for task. +required |







### TaskCreateResponse {#flyteidl-admin-TaskCreateResponse}
Represents a response structure if task creation succeeds.

Purposefully empty, may be populated in the future.







### TaskList {#flyteidl-admin-TaskList}
Represents a list of tasks returned from the admin.
See :ref:`ref_flyteidl.admin.Task` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tasks | [Task](#flyteidl-admin-Task) | repeated | A list of tasks returned based on the request. |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### TaskSpec {#flyteidl-admin-TaskSpec}
Represents a structure that encapsulates the user-configured specification of the task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| template | [flyteidl.core.TaskTemplate](#flyteidl-core-TaskTemplate) |  | Template of the task that encapsulates all the metadata of the task. |
| description | [DescriptionEntity](#flyteidl-admin-DescriptionEntity) |  | Represents the specification for description entity. |
















## flyteidl/admin/launch_plan.proto




### ActiveLaunchPlanListRequest {#flyteidl-admin-ActiveLaunchPlanListRequest}
Represents a request structure to list active launch plans within a project/domain and optional org.
See :ref:`ref_flyteidl.admin.LaunchPlan` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Name of the project that contains the identifiers. +required. |
| domain | string |  | Name of the domain the identifiers belongs to within the project. +required. |
| limit | uint32 |  | Indicates the number of resources to be returned. +required. |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Sort ordering. +optional |
| org | string |  | Optional, org key applied to the resource. |







### ActiveLaunchPlanRequest {#flyteidl-admin-ActiveLaunchPlanRequest}
Represents a request struct for finding an active launch plan for a given NamedEntityIdentifier
See :ref:`ref_flyteidl.admin.LaunchPlan` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [NamedEntityIdentifier](#flyteidl-admin-NamedEntityIdentifier) |  | +required. |







### Auth {#flyteidl-admin-Auth}
Defines permissions associated with executions created by this launch plan spec.
Use either of these roles when they have permissions required by your workflow execution.
Deprecated.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| assumable_iam_role | string |  | Defines an optional iam role which will be used for tasks run in executions created with this launch plan. |
| kubernetes_service_account | string |  | Defines an optional kubernetes service account which will be used for tasks run in executions created with this launch plan. |







### LaunchPlan {#flyteidl-admin-LaunchPlan}
A LaunchPlan provides the capability to templatize workflow executions.
Launch plans simplify associating one or more schedules, inputs and notifications with your workflows.
Launch plans can be shared and used to trigger executions with predefined inputs even when a workflow
definition doesn't necessarily have a default value for said input.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | Uniquely identifies a launch plan entity. |
| spec | [LaunchPlanSpec](#flyteidl-admin-LaunchPlanSpec) |  | User-provided launch plan details, including reference workflow, inputs and other metadata. |
| closure | [LaunchPlanClosure](#flyteidl-admin-LaunchPlanClosure) |  | Values computed by the flyte platform after launch plan registration. |







### LaunchPlanClosure {#flyteidl-admin-LaunchPlanClosure}
Values computed by the flyte platform after launch plan registration.
These include expected_inputs required to be present in a CreateExecutionRequest
to launch the reference workflow as well timestamp values associated with the launch plan.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [LaunchPlanState](#flyteidl-admin-LaunchPlanState) |  | Indicate the Launch plan state. |
| expected_inputs | [flyteidl.core.ParameterMap](#flyteidl-core-ParameterMap) |  | Indicates the set of inputs expected when creating an execution with the Launch plan |
| expected_outputs | [flyteidl.core.VariableMap](#flyteidl-core-VariableMap) |  | Indicates the set of outputs expected to be produced by creating an execution with the Launch plan |
| created_at | google.protobuf.Timestamp |  | Time at which the launch plan was created. |
| updated_at | google.protobuf.Timestamp |  | Time at which the launch plan was last updated. |







### LaunchPlanCreateRequest {#flyteidl-admin-LaunchPlanCreateRequest}
Request to register a launch plan. The included LaunchPlanSpec may have a complete or incomplete set of inputs required
to launch a workflow execution. By default all launch plans are registered in state INACTIVE. If you wish to
set the state to ACTIVE, you must submit a LaunchPlanUpdateRequest, after you have successfully created a launch plan.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | Uniquely identifies a launch plan entity. |
| spec | [LaunchPlanSpec](#flyteidl-admin-LaunchPlanSpec) |  | User-provided launch plan details, including reference workflow, inputs and other metadata. |







### LaunchPlanCreateResponse {#flyteidl-admin-LaunchPlanCreateResponse}
Purposefully empty, may be populated in the future.







### LaunchPlanList {#flyteidl-admin-LaunchPlanList}
Response object for list launch plan requests.
See :ref:`ref_flyteidl.admin.LaunchPlan` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| launch_plans | [LaunchPlan](#flyteidl-admin-LaunchPlan) | repeated |  |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### LaunchPlanMetadata {#flyteidl-admin-LaunchPlanMetadata}
Additional launch plan attributes included in the LaunchPlanSpec not strictly required to launch
the reference workflow.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| schedule | [Schedule](#flyteidl-admin-Schedule) |  | Schedule to execute the Launch Plan |
| notifications | [Notification](#flyteidl-admin-Notification) | repeated | List of notifications based on Execution status transitions |
| launch_conditions | google.protobuf.Any |  | Additional metadata for how to launch the launch plan |







### LaunchPlanSpec {#flyteidl-admin-LaunchPlanSpec}
User-provided launch plan definition and configuration values.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| workflow_id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | Reference to the Workflow template that the launch plan references |
| entity_metadata | [LaunchPlanMetadata](#flyteidl-admin-LaunchPlanMetadata) |  | Metadata for the Launch Plan |
| default_inputs | [flyteidl.core.ParameterMap](#flyteidl-core-ParameterMap) |  | Input values to be passed for the execution. These can be overridden when an execution is created with this launch plan. |
| fixed_inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Fixed, non-overridable inputs for the Launch Plan. These can not be overridden when an execution is created with this launch plan. |
| role | string |  | **Deprecated.** String to indicate the role to use to execute the workflow underneath |
| labels | [Labels](#flyteidl-admin-Labels) |  | Custom labels to be applied to the execution resource. |
| annotations | [Annotations](#flyteidl-admin-Annotations) |  | Custom annotations to be applied to the execution resource. |
| auth | [Auth](#flyteidl-admin-Auth) |  | **Deprecated.** Indicates the permission associated with workflow executions triggered with this launch plan. |
| auth_role | [AuthRole](#flyteidl-admin-AuthRole) |  | **Deprecated.**  |
| security_context | [flyteidl.core.SecurityContext](#flyteidl-core-SecurityContext) |  | Indicates security context for permissions triggered with this launch plan |
| quality_of_service | [flyteidl.core.QualityOfService](#flyteidl-core-QualityOfService) |  | Indicates the runtime priority of the execution. |
| raw_output_data_config | [RawOutputDataConfig](#flyteidl-admin-RawOutputDataConfig) |  | Encapsulates user settings pertaining to offloaded data (i.e. Blobs, Schema, query data, etc.). |
| max_parallelism | int32 |  | Controls the maximum number of tasknodes that can be run in parallel for the entire workflow. This is useful to achieve fairness. Note: MapTasks are regarded as one unit, and parallelism/concurrency of MapTasks is independent from this. |
| interruptible | google.protobuf.BoolValue |  | Allows for the interruptible flag of a workflow to be overwritten for a single execution. Omitting this field uses the workflow's value as a default. As we need to distinguish between the field not being provided and its default value false, we have to use a wrapper around the bool field. |
| overwrite_cache | bool |  | Allows for all cached values of a workflow and its tasks to be overwritten for a single execution. If enabled, all calculations are performed even if cached results would be available, overwriting the stored data once execution finishes successfully. |
| envs | [Envs](#flyteidl-admin-Envs) |  | Environment variables to be set for the execution. |
| execution_env_assignments | [flyteidl.core.ExecutionEnvAssignment](#flyteidl-core-ExecutionEnvAssignment) | repeated | Execution environment assignments to be set for the execution. |
| cluster_assignment | [ClusterAssignment](#flyteidl-admin-ClusterAssignment) |  | ClusterAssignment controls how to select an available cluster on which executions of this LaunchPlan should run. This can be overwritten at execution creation level. |







### LaunchPlanUpdateRequest {#flyteidl-admin-LaunchPlanUpdateRequest}
Request to set the referenced launch plan state to the configured value.
See :ref:`ref_flyteidl.admin.LaunchPlan` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | Identifier of launch plan for which to change state. +required. |
| state | [LaunchPlanState](#flyteidl-admin-LaunchPlanState) |  | Desired state to apply to the launch plan. +required. |







### LaunchPlanUpdateResponse {#flyteidl-admin-LaunchPlanUpdateResponse}
Purposefully empty, may be populated in the future.









### LaunchPlanState {#flyteidl-admin-LaunchPlanState}
By default any launch plan regardless of state can be used to launch a workflow execution.
However, at most one version of a launch plan
(e.g. a NamedEntityIdentifier set of shared project, domain and name values) can be
active at a time in regards to *schedules*. That is, at most one schedule in a NamedEntityIdentifier
group will be observed and trigger executions at a defined cadence.

| Name | Number | Description |
| ---- | ------ | ----------- |
| INACTIVE | 0 |  |
| ACTIVE | 1 |  |











## flyteidl/admin/signal.proto




### Signal {#flyteidl-admin-Signal}
Signal encapsulates a unique identifier, associated metadata, and a value for a single Flyte
signal. Signals may exist either without a set value (representing a signal request) or with a
populated value (indicating the signal has been given).



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.SignalIdentifier](#flyteidl-core-SignalIdentifier) |  | A unique identifier for the requested signal. |
| type | [flyteidl.core.LiteralType](#flyteidl-core-LiteralType) |  | A type denoting the required value type for this signal. |
| value | [flyteidl.core.Literal](#flyteidl-core-Literal) |  | The value of the signal. This is only available if the signal has been "set" and must match the defined the type. |







### SignalGetOrCreateRequest {#flyteidl-admin-SignalGetOrCreateRequest}
SignalGetOrCreateRequest represents a request structure to retrieve or create a signal.
See :ref:`ref_flyteidl.admin.Signal` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.SignalIdentifier](#flyteidl-core-SignalIdentifier) |  | A unique identifier for the requested signal. |
| type | [flyteidl.core.LiteralType](#flyteidl-core-LiteralType) |  | A type denoting the required value type for this signal. |







### SignalList {#flyteidl-admin-SignalList}
SignalList represents collection of signals along with the token of the last result.
See :ref:`ref_flyteidl.admin.Signal` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signals | [Signal](#flyteidl-admin-Signal) | repeated | A list of signals matching the input filters. |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### SignalListRequest {#flyteidl-admin-SignalListRequest}
SignalListRequest represents a request structure to retrieve a collection of signals.
See :ref:`ref_flyteidl.admin.Signal` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| workflow_execution_id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Indicates the workflow execution to filter by. +required |
| limit | uint32 |  | Indicates the number of resources to be returned. +required |
| token | string |  | In the case of multiple pages of results, the, server-provided token can be used to fetch the next page in a query. +optional |
| filters | string |  | Indicates a list of filters passed as string. +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Sort ordering. +optional |







### SignalSetRequest {#flyteidl-admin-SignalSetRequest}
SignalSetRequest represents a request structure to set the value on a signal. Setting a signal
effetively satisfies the signal condition within a Flyte workflow.
See :ref:`ref_flyteidl.admin.Signal` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.SignalIdentifier](#flyteidl-core-SignalIdentifier) |  | A unique identifier for the requested signal. |
| value | [flyteidl.core.Literal](#flyteidl-core-Literal) |  | The value of this signal, must match the defining signal type. |







### SignalSetResponse {#flyteidl-admin-SignalSetResponse}
SignalSetResponse represents a response structure if signal setting succeeds.

Purposefully empty, may be populated in the future.
















## flyteidl/admin/task_execution.proto




### Reason {#flyteidl-admin-Reason}
Reason is a single message annotated with a timestamp to indicate the instant the reason occurred.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| occurred_at | google.protobuf.Timestamp |  | occurred_at is the timestamp indicating the instant that this reason happened. |
| message | string |  | message is the explanation for the most recent phase transition or status update. |







### TaskExecution {#flyteidl-admin-TaskExecution}
Encapsulates all details for a single task execution entity.
A task execution represents an instantiated task, including all inputs and additional
metadata as well as computed results included state, outputs, and duration-based attributes.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  | Unique identifier for the task execution. |
| input_uri | string |  | Path to remote data store where input blob is stored. |
| closure | [TaskExecutionClosure](#flyteidl-admin-TaskExecutionClosure) |  | Task execution details and results. |
| is_parent | bool |  | Whether this task spawned nodes. |







### TaskExecutionClosure {#flyteidl-admin-TaskExecutionClosure}
Container for task execution details and results.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| output_uri | string |  | **Deprecated.** Path to remote data store where output blob is stored if the execution succeeded (and produced outputs). DEPRECATED. Use GetTaskExecutionData to fetch output data instead. |
| error | [flyteidl.core.ExecutionError](#flyteidl-core-ExecutionError) |  | Error information for the task execution. Populated if the execution failed. |
| output_data | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | **Deprecated.** Raw output data produced by this task execution. DEPRECATED. Use GetTaskExecutionData to fetch output data instead. |
| phase | [flyteidl.core.TaskExecution.Phase](#flyteidl-core-TaskExecution-Phase) |  | The last recorded phase for this task execution. |
| logs | [flyteidl.core.TaskLog](#flyteidl-core-TaskLog) | repeated | Detailed log information output by the task execution. |
| started_at | google.protobuf.Timestamp |  | Time at which the task execution began running. |
| duration | google.protobuf.Duration |  | The amount of time the task execution spent running. |
| created_at | google.protobuf.Timestamp |  | Time at which the task execution was created. |
| updated_at | google.protobuf.Timestamp |  | Time at which the task execution was last updated. |
| custom_info | google.protobuf.Struct |  | Custom data specific to the task plugin. |
| reason | string |  | If there is an explanation for the most recent phase transition, the reason will capture it. |
| task_type | string |  | A predefined yet extensible Task type identifier. |
| metadata | [flyteidl.event.TaskExecutionMetadata](#flyteidl-event-TaskExecutionMetadata) |  | Metadata around how a task was executed. |
| event_version | int32 |  | The event version is used to indicate versioned changes in how data is maintained using this proto message. For example, event_verison >gt; 0 means that maps tasks logs use the TaskExecutionMetadata ExternalResourceInfo fields for each subtask rather than the TaskLog in this message. |
| reasons | [Reason](#flyteidl-admin-Reason) | repeated | A time-series of the phase transition or update explanations. This, when compared to storing a singular reason as previously done, is much more valuable in visualizing and understanding historical evaluations. |







### TaskExecutionGetDataRequest {#flyteidl-admin-TaskExecutionGetDataRequest}
Request structure to fetch inputs and output for a task execution.
By default this data is not returned inline in :ref:`ref_flyteidl.admin.TaskExecutionGetRequest`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  | The identifier of the task execution for which to fetch inputs and outputs. +required |







### TaskExecutionGetDataResponse {#flyteidl-admin-TaskExecutionGetDataResponse}
Response structure for TaskExecutionGetDataRequest which contains inputs and outputs for a task execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inputs | [UrlBlob](#flyteidl-admin-UrlBlob) |  | **Deprecated.** Signed url to fetch a core.LiteralMap of task execution inputs. Deprecated: Please use full_inputs instead. |
| outputs | [UrlBlob](#flyteidl-admin-UrlBlob) |  | **Deprecated.** Signed url to fetch a core.LiteralMap of task execution outputs. Deprecated: Please use full_outputs instead. |
| full_inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Full_inputs will only be populated if they are under a configured size threshold. |
| full_outputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Full_outputs will only be populated if they are under a configured size threshold. |
| flyte_urls | [FlyteURLs](#flyteidl-admin-FlyteURLs) |  | flyte tiny url to fetch a core.LiteralMap of task execution's IO Deck will be empty for task |







### TaskExecutionGetRequest {#flyteidl-admin-TaskExecutionGetRequest}
A message used to fetch a single task execution entity.
See :ref:`ref_flyteidl.admin.TaskExecution` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  | Unique identifier for the task execution. +required |







### TaskExecutionList {#flyteidl-admin-TaskExecutionList}
Response structure for a query to list of task execution entities.
See :ref:`ref_flyteidl.admin.TaskExecution` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_executions | [TaskExecution](#flyteidl-admin-TaskExecution) | repeated |  |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### TaskExecutionListRequest {#flyteidl-admin-TaskExecutionListRequest}
Represents a request structure to retrieve a list of task execution entities yielded by a specific node execution.
See :ref:`ref_flyteidl.admin.TaskExecution` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_execution_id | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | Indicates the node execution to filter by. +required |
| limit | uint32 |  | Indicates the number of resources to be returned. +required |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. +optional |
| filters | string |  | Indicates a list of filters passed as string. More info on constructing filters : <lt;Link>gt; +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Sort ordering for returned list. +optional |
















## flyteidl/admin/node_execution.proto




### DynamicNodeWorkflowResponse {#flyteidl-admin-DynamicNodeWorkflowResponse}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| compiled_workflow | [flyteidl.core.CompiledWorkflowClosure](#flyteidl-core-CompiledWorkflowClosure) |  |  |







### DynamicWorkflowNodeMetadata {#flyteidl-admin-DynamicWorkflowNodeMetadata}
For dynamic workflow nodes we capture information about the dynamic workflow definition that gets generated.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | id represents the unique identifier of the workflow. |
| compiled_workflow | [flyteidl.core.CompiledWorkflowClosure](#flyteidl-core-CompiledWorkflowClosure) |  | Represents the compiled representation of the embedded dynamic workflow. |
| dynamic_job_spec_uri | string |  | dynamic_job_spec_uri is the location of the DynamicJobSpec proto message for this DynamicWorkflow. This is required to correctly recover partially completed executions where the subworkflow has already been compiled. |







### GetDynamicNodeWorkflowRequest {#flyteidl-admin-GetDynamicNodeWorkflowRequest}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  |  |







### NodeExecution {#flyteidl-admin-NodeExecution}
Encapsulates all details for a single node execution entity.
A node represents a component in the overall workflow graph. A node launch a task, multiple tasks, an entire nested
sub-workflow, or even a separate child-workflow execution.
The same task can be called repeatedly in a single workflow but each node is unique.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | Uniquely identifies an individual node execution. |
| input_uri | string |  | Path to remote data store where input blob is stored. |
| closure | [NodeExecutionClosure](#flyteidl-admin-NodeExecutionClosure) |  | Computed results associated with this node execution. |
| metadata | [NodeExecutionMetaData](#flyteidl-admin-NodeExecutionMetaData) |  | Metadata for Node Execution |







### NodeExecutionClosure {#flyteidl-admin-NodeExecutionClosure}
Container for node execution details and results.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| output_uri | string |  | **Deprecated.** Links to a remotely stored, serialized core.LiteralMap of node execution outputs. DEPRECATED. Use GetNodeExecutionData to fetch output data instead. |
| error | [flyteidl.core.ExecutionError](#flyteidl-core-ExecutionError) |  | Error information for the Node |
| output_data | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | **Deprecated.** Raw output data produced by this node execution. DEPRECATED. Use GetNodeExecutionData to fetch output data instead. |
| phase | [flyteidl.core.NodeExecution.Phase](#flyteidl-core-NodeExecution-Phase) |  | The last recorded phase for this node execution. |
| started_at | google.protobuf.Timestamp |  | Time at which the node execution began running. |
| duration | google.protobuf.Duration |  | The amount of time the node execution spent running. |
| created_at | google.protobuf.Timestamp |  | Time at which the node execution was created. |
| updated_at | google.protobuf.Timestamp |  | Time at which the node execution was last updated. |
| workflow_node_metadata | [WorkflowNodeMetadata](#flyteidl-admin-WorkflowNodeMetadata) |  |  |
| task_node_metadata | [TaskNodeMetadata](#flyteidl-admin-TaskNodeMetadata) |  |  |
| deck_uri | string |  | String location uniquely identifying where the deck HTML file is. NativeUrl specifies the url in the format of the configured storage provider (e.g. s3://my-bucket/randomstring/suffix.tar) |
| dynamic_job_spec_uri | string |  | dynamic_job_spec_uri is the location of the DynamicJobSpec proto message for a DynamicWorkflow. This is required to correctly recover partially completed executions where the subworkflow has already been compiled. |







### NodeExecutionForTaskListRequest {#flyteidl-admin-NodeExecutionForTaskListRequest}
Represents a request structure to retrieve a list of node execution entities launched by a specific task.
This can arise when a task yields a subworkflow.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_execution_id | [flyteidl.core.TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  | Indicates the node execution to filter by. +required |
| limit | uint32 |  | Indicates the number of resources to be returned. +required |
| token | string |  | In the case of multiple pages of results, the, server-provided token can be used to fetch the next page in a query. +optional |
| filters | string |  | Indicates a list of filters passed as string. More info on constructing filters : <lt;Link>gt; +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Sort ordering. +optional |







### NodeExecutionGetDataRequest {#flyteidl-admin-NodeExecutionGetDataRequest}
Request structure to fetch inputs and output for a node execution.
By default, these are not returned in :ref:`ref_flyteidl.admin.NodeExecutionGetRequest`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | The identifier of the node execution for which to fetch inputs and outputs. |







### NodeExecutionGetDataResponse {#flyteidl-admin-NodeExecutionGetDataResponse}
Response structure for NodeExecutionGetDataRequest which contains inputs and outputs for a node execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inputs | [UrlBlob](#flyteidl-admin-UrlBlob) |  | **Deprecated.** Signed url to fetch a core.LiteralMap of node execution inputs. Deprecated: Please use full_inputs instead. |
| outputs | [UrlBlob](#flyteidl-admin-UrlBlob) |  | **Deprecated.** Signed url to fetch a core.LiteralMap of node execution outputs. Deprecated: Please use full_outputs instead. |
| full_inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Full_inputs will only be populated if they are under a configured size threshold. |
| full_outputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Full_outputs will only be populated if they are under a configured size threshold. |
| dynamic_workflow | [DynamicWorkflowNodeMetadata](#flyteidl-admin-DynamicWorkflowNodeMetadata) |  | Optional Workflow closure for a dynamically generated workflow, in the case this node yields a dynamic workflow we return its structure here. |
| flyte_urls | [FlyteURLs](#flyteidl-admin-FlyteURLs) |  |  |







### NodeExecutionGetRequest {#flyteidl-admin-NodeExecutionGetRequest}
A message used to fetch a single node execution entity.
See :ref:`ref_flyteidl.admin.NodeExecution` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | Uniquely identifies an individual node execution. +required |







### NodeExecutionList {#flyteidl-admin-NodeExecutionList}
Request structure to retrieve a list of node execution entities.
See :ref:`ref_flyteidl.admin.NodeExecution` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_executions | [NodeExecution](#flyteidl-admin-NodeExecution) | repeated |  |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### NodeExecutionListRequest {#flyteidl-admin-NodeExecutionListRequest}
Represents a request structure to retrieve a list of node execution entities.
See :ref:`ref_flyteidl.admin.NodeExecution` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| workflow_execution_id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Indicates the workflow execution to filter by. +required |
| limit | uint32 |  | Indicates the number of resources to be returned. +required |
| token | string |  |  |
| filters | string |  | Indicates a list of filters passed as string. More info on constructing filters : <lt;Link>gt; +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Sort ordering. +optional |
| unique_parent_id | string |  | Unique identifier of the parent node in the execution +optional |







### NodeExecutionMetaData {#flyteidl-admin-NodeExecutionMetaData}
Represents additional attributes related to a Node Execution



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| retry_group | string |  | Node executions are grouped depending on retries of the parent Retry group is unique within the context of a parent node. |
| is_parent_node | bool |  | Boolean flag indicating if the node has child nodes under it This can be true when a node contains a dynamic workflow which then produces child nodes. |
| spec_node_id | string |  | Node id of the node in the original workflow This maps to value of WorkflowTemplate.nodes[X].id |
| is_dynamic | bool |  | Boolean flag indicating if the node has contains a dynamic workflow which then produces child nodes. This is to distinguish between subworkflows and dynamic workflows which can both have is_parent_node as true. |
| is_array | bool |  | Boolean flag indicating if the node is an array node. This is intended to uniquely identify array nodes from other nodes which can have is_parent_node as true. |
| is_eager | bool |  | Whether this node is an eager node. |







### TaskNodeMetadata {#flyteidl-admin-TaskNodeMetadata}
Metadata for the case in which the node is a TaskNode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cache_status | [flyteidl.core.CatalogCacheStatus](#flyteidl-core-CatalogCacheStatus) |  | Captures the status of caching for this execution. |
| catalog_key | [flyteidl.core.CatalogMetadata](#flyteidl-core-CatalogMetadata) |  | This structure carries the catalog artifact information |
| checkpoint_uri | string |  | The latest checkpoint location |







### WorkflowNodeMetadata {#flyteidl-admin-WorkflowNodeMetadata}
Metadata for a WorkflowNode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| executionId | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | The identifier for a workflow execution launched by a node. |
















## flyteidl/admin/execution.proto




### AbortMetadata {#flyteidl-admin-AbortMetadata}
Specifies metadata around an aborted workflow execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cause | string |  | In the case of a user-specified abort, this will pass along the user-supplied cause. |
| principal | string |  | Identifies the entity (if any) responsible for terminating the execution |







### Execution {#flyteidl-admin-Execution}
A workflow execution represents an instantiated workflow, including all inputs and additional
metadata as well as computed results included state, outputs, and duration-based attributes.
Used as a response object used in Get and List execution requests.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Unique identifier of the workflow execution. |
| spec | [ExecutionSpec](#flyteidl-admin-ExecutionSpec) |  | User-provided configuration and inputs for launching the execution. |
| closure | [ExecutionClosure](#flyteidl-admin-ExecutionClosure) |  | Execution results. |







### ExecutionClosure {#flyteidl-admin-ExecutionClosure}
Encapsulates the results of the Execution



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| outputs | [LiteralMapBlob](#flyteidl-admin-LiteralMapBlob) |  | **Deprecated.** Output URI in the case of a successful execution. DEPRECATED. Use GetExecutionData to fetch output data instead. |
| error | [flyteidl.core.ExecutionError](#flyteidl-core-ExecutionError) |  | Error information in the case of a failed execution. |
| abort_cause | string |  | **Deprecated.** In the case of a user-specified abort, this will pass along the user-supplied cause. |
| abort_metadata | [AbortMetadata](#flyteidl-admin-AbortMetadata) |  | In the case of a user-specified abort, this will pass along the user and their supplied cause. |
| output_data | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | **Deprecated.** Raw output data produced by this execution. DEPRECATED. Use GetExecutionData to fetch output data instead. |
| computed_inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | **Deprecated.** Inputs computed and passed for execution. computed_inputs depends on inputs in ExecutionSpec, fixed and default inputs in launch plan |
| phase | [flyteidl.core.WorkflowExecution.Phase](#flyteidl-core-WorkflowExecution-Phase) |  | Most recent recorded phase for the execution. |
| started_at | google.protobuf.Timestamp |  | Reported time at which the execution began running. |
| duration | google.protobuf.Duration |  | The amount of time the execution spent running. |
| created_at | google.protobuf.Timestamp |  | Reported time at which the execution was created. |
| updated_at | google.protobuf.Timestamp |  | Reported time at which the execution was last updated. |
| notifications | [Notification](#flyteidl-admin-Notification) | repeated | The notification settings to use after merging the CreateExecutionRequest and the launch plan notification settings. An execution launched with notifications will always prefer that definition to notifications defined statically in a launch plan. |
| workflow_id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | Identifies the workflow definition for this execution. |
| state_change_details | [ExecutionStateChangeDetails](#flyteidl-admin-ExecutionStateChangeDetails) |  | Provides the details of the last stage change |







### ExecutionCreateRequest {#flyteidl-admin-ExecutionCreateRequest}
Request to launch an execution with the given project, domain and optionally-assigned name.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Name of the project the execution belongs to. +required |
| domain | string |  | Name of the domain the execution belongs to. A domain can be considered as a subset within a specific project. +required |
| name | string |  | User provided value for the resource. If none is provided the system will generate a unique string. +optional |
| spec | [ExecutionSpec](#flyteidl-admin-ExecutionSpec) |  | Additional fields necessary to launch the execution. +optional |
| inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | The inputs required to start the execution. All required inputs must be included in this map. If not required and not provided, defaults apply. +optional |
| org | string |  | Optional, org key applied to the resource. |







### ExecutionCreateResponse {#flyteidl-admin-ExecutionCreateResponse}
The unique identifier for a successfully created execution.
If the name was *not* specified in the create request, this identifier will include a generated name.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  |  |







### ExecutionList {#flyteidl-admin-ExecutionList}
Used as a response for request to list executions.
See :ref:`ref_flyteidl.admin.Execution` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| executions | [Execution](#flyteidl-admin-Execution) | repeated |  |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### ExecutionMetadata {#flyteidl-admin-ExecutionMetadata}
Represents attributes about an execution which are not required to launch the execution but are useful to record.
These attributes are assigned at launch time and do not change.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mode | [ExecutionMetadata.ExecutionMode](#flyteidl-admin-ExecutionMetadata-ExecutionMode) |  |  |
| principal | string |  | Identifier of the entity that triggered this execution. For systems using back-end authentication any value set here will be discarded in favor of the authenticated user context. |
| nesting | uint32 |  | Indicates the nestedness of this execution. If a user launches a workflow execution, the default nesting is 0. If this execution further launches a workflow (child workflow), the nesting level is incremented by 0 =>gt; 1 Generally, if workflow at nesting level k launches a workflow then the child workflow will have nesting = k + 1. |
| scheduled_at | google.protobuf.Timestamp |  | For scheduled executions, the requested time for execution for this specific schedule invocation. |
| parent_node_execution | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | Which subworkflow node (if any) launched this execution |
| reference_execution | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Optional, a reference workflow execution related to this execution. In the case of a relaunch, this references the original workflow execution. |
| system_metadata | [SystemMetadata](#flyteidl-admin-SystemMetadata) |  | Optional, platform-specific metadata about the execution. In this the future this may be gated behind an ACL or some sort of authorization. |
| artifact_ids | [flyteidl.core.ArtifactID](#flyteidl-core-ArtifactID) | repeated | Save a list of the artifacts used in this execution for now. This is a list only rather than a mapping since we don't have a structure to handle nested ones anyways. |







### ExecutionRecoverRequest {#flyteidl-admin-ExecutionRecoverRequest}
Request to recover the referenced execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Identifier of the workflow execution to recover. |
| name | string |  | User provided value for the recovered execution. If none is provided the system will generate a unique string. +optional |
| metadata | [ExecutionMetadata](#flyteidl-admin-ExecutionMetadata) |  | Additional metadata which will be used to overwrite any metadata in the reference execution when triggering a recovery execution. |







### ExecutionRelaunchRequest {#flyteidl-admin-ExecutionRelaunchRequest}
Request to relaunch the referenced execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Identifier of the workflow execution to relaunch. +required |
| name | string |  | User provided value for the relaunched execution. If none is provided the system will generate a unique string. +optional |
| overwrite_cache | bool |  | Allows for all cached values of a workflow and its tasks to be overwritten for a single execution. If enabled, all calculations are performed even if cached results would be available, overwriting the stored data once execution finishes successfully. |







### ExecutionSpec {#flyteidl-admin-ExecutionSpec}
An ExecutionSpec encompasses all data used to launch this execution. The Spec does not change over the lifetime
of an execution as it progresses across phase changes.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| launch_plan | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | Launch plan to be executed |
| inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | **Deprecated.** Input values to be passed for the execution |
| metadata | [ExecutionMetadata](#flyteidl-admin-ExecutionMetadata) |  | Metadata for the execution |
| notifications | [NotificationList](#flyteidl-admin-NotificationList) |  | List of notifications based on Execution status transitions When this list is not empty it is used rather than any notifications defined in the referenced launch plan. When this list is empty, the notifications defined for the launch plan will be applied. |
| disable_all | bool |  | This should be set to true if all notifications are intended to be disabled for this execution. |
| labels | [Labels](#flyteidl-admin-Labels) |  | Labels to apply to the execution resource. |
| annotations | [Annotations](#flyteidl-admin-Annotations) |  | Annotations to apply to the execution resource. |
| security_context | [flyteidl.core.SecurityContext](#flyteidl-core-SecurityContext) |  | Optional: security context override to apply this execution. |
| auth_role | [AuthRole](#flyteidl-admin-AuthRole) |  | **Deprecated.** Optional: auth override to apply this execution. |
| quality_of_service | [flyteidl.core.QualityOfService](#flyteidl-core-QualityOfService) |  | Indicates the runtime priority of the execution. |
| max_parallelism | int32 |  | Controls the maximum number of task nodes that can be run in parallel for the entire workflow. This is useful to achieve fairness. Note: MapTasks are regarded as one unit, and parallelism/concurrency of MapTasks is independent from this. |
| raw_output_data_config | [RawOutputDataConfig](#flyteidl-admin-RawOutputDataConfig) |  | User setting to configure where to store offloaded data (i.e. Blobs, structured datasets, query data, etc.). This should be a prefix like s3://my-bucket/my-data |
| cluster_assignment | [ClusterAssignment](#flyteidl-admin-ClusterAssignment) |  | Controls how to select an available cluster on which this execution should run. |
| interruptible | google.protobuf.BoolValue |  | Allows for the interruptible flag of a workflow to be overwritten for a single execution. Omitting this field uses the workflow's value as a default. As we need to distinguish between the field not being provided and its default value false, we have to use a wrapper around the bool field. |
| overwrite_cache | bool |  | Allows for all cached values of a workflow and its tasks to be overwritten for a single execution. If enabled, all calculations are performed even if cached results would be available, overwriting the stored data once execution finishes successfully. |
| envs | [Envs](#flyteidl-admin-Envs) |  | Environment variables to be set for the execution. |
| tags | string | repeated | **Deprecated.** Tags to be set for the execution. |
| execution_cluster_label | [ExecutionClusterLabel](#flyteidl-admin-ExecutionClusterLabel) |  | Execution cluster label to be set for the execution. |
| execution_env_assignments | [flyteidl.core.ExecutionEnvAssignment](#flyteidl-core-ExecutionEnvAssignment) | repeated | Execution environment assignments to be set for the execution. |







### ExecutionStateChangeDetails {#flyteidl-admin-ExecutionStateChangeDetails}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [ExecutionState](#flyteidl-admin-ExecutionState) |  | The state of the execution is used to control its visibility in the UI/CLI. |
| occurred_at | google.protobuf.Timestamp |  | This timestamp represents when the state changed. |
| principal | string |  | Identifies the entity (if any) responsible for causing the state change of the execution |







### ExecutionTerminateRequest {#flyteidl-admin-ExecutionTerminateRequest}
Request to terminate an in-progress execution.  This action is irreversible.
If an execution is already terminated, this request will simply be a no-op.
This request will fail if it references a non-existent execution.
If the request succeeds the phase "ABORTED" will be recorded for the termination
with the optional cause added to the output_result.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Uniquely identifies the individual workflow execution to be terminated. |
| cause | string |  | Optional reason for aborting. |







### ExecutionTerminateResponse {#flyteidl-admin-ExecutionTerminateResponse}
Purposefully empty, may be populated in the future.







### ExecutionUpdateRequest {#flyteidl-admin-ExecutionUpdateRequest}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Identifier of the execution to update |
| state | [ExecutionState](#flyteidl-admin-ExecutionState) |  | State to set as the new value active/archive |







### ExecutionUpdateResponse {#flyteidl-admin-ExecutionUpdateResponse}








### LiteralMapBlob {#flyteidl-admin-LiteralMapBlob}
Input/output data can represented by actual values or a link to where values are stored



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | **Deprecated.** Data in LiteralMap format |
| uri | string |  | In the event that the map is too large, we return a uri to the data |







### NotificationList {#flyteidl-admin-NotificationList}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| notifications | [Notification](#flyteidl-admin-Notification) | repeated |  |







### SystemMetadata {#flyteidl-admin-SystemMetadata}
Represents system, rather than user-facing, metadata about an execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| execution_cluster | string |  | Which execution cluster this execution ran on. |
| namespace | string |  | Which kubernetes namespace the execution ran under. |







### WorkflowExecutionGetDataRequest {#flyteidl-admin-WorkflowExecutionGetDataRequest}
Request structure to fetch inputs, output and other data produced by an execution.
By default this data is not returned inline in :ref:`ref_flyteidl.admin.WorkflowExecutionGetRequest`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | The identifier of the execution for which to fetch inputs and outputs. |







### WorkflowExecutionGetDataResponse {#flyteidl-admin-WorkflowExecutionGetDataResponse}
Response structure for WorkflowExecutionGetDataRequest which contains inputs and outputs for an execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| outputs | [UrlBlob](#flyteidl-admin-UrlBlob) |  | **Deprecated.** Signed url to fetch a core.LiteralMap of execution outputs. Deprecated: Please use full_outputs instead. |
| inputs | [UrlBlob](#flyteidl-admin-UrlBlob) |  | **Deprecated.** Signed url to fetch a core.LiteralMap of execution inputs. Deprecated: Please use full_inputs instead. |
| full_inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Full_inputs will only be populated if they are under a configured size threshold. |
| full_outputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Full_outputs will only be populated if they are under a configured size threshold. |







### WorkflowExecutionGetMetricsRequest {#flyteidl-admin-WorkflowExecutionGetMetricsRequest}
WorkflowExecutionGetMetricsRequest represents a request to retrieve metrics for the specified workflow execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | id defines the workflow execution to query for. |
| depth | int32 |  | depth defines the number of Flyte entity levels to traverse when breaking down execution details. |







### WorkflowExecutionGetMetricsResponse {#flyteidl-admin-WorkflowExecutionGetMetricsResponse}
WorkflowExecutionGetMetricsResponse represents the response containing metrics for the specified workflow execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| span | [flyteidl.core.Span](#flyteidl-core-Span) |  | Span defines the top-level breakdown of the workflows execution. More precise information is nested in a hierarchical structure using Flyte entity references. |







### WorkflowExecutionGetRequest {#flyteidl-admin-WorkflowExecutionGetRequest}
A message used to fetch a single workflow execution entity.
See :ref:`ref_flyteidl.admin.Execution` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Uniquely identifies an individual workflow execution. |









### ExecutionMetadata.ExecutionMode {#flyteidl-admin-ExecutionMetadata-ExecutionMode}
The method by which this execution was launched.

| Name | Number | Description |
| ---- | ------ | ----------- |
| MANUAL | 0 | The default execution mode, MANUAL implies that an execution was launched by an individual. |
| SCHEDULED | 1 | A schedule triggered this execution launch. |
| SYSTEM | 2 | A system process was responsible for launching this execution rather an individual. |
| RELAUNCH | 3 | This execution was launched with identical inputs as a previous execution. |
| CHILD_WORKFLOW | 4 | This execution was triggered by another execution. |
| RECOVERED | 5 | This execution was recovered from another execution. |
| TRIGGER | 6 | Execution was kicked off by the artifact trigger system |




### ExecutionState {#flyteidl-admin-ExecutionState}
The state of the execution is used to control its visibility in the UI/CLI.

| Name | Number | Description |
| ---- | ------ | ----------- |
| EXECUTION_ACTIVE | 0 | By default, all executions are considered active. |
| EXECUTION_ARCHIVED | 1 | Archived executions are no longer visible in the UI. |











## flyteidl/admin/workflow_attributes.proto




### WorkflowAttributes {#flyteidl-admin-WorkflowAttributes}
Defines a set of custom matching attributes which defines resource defaults for a project, domain and workflow.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id for which this set of attributes will be applied. |
| domain | string |  | Unique domain id for which this set of attributes will be applied. |
| workflow | string |  | Workflow name for which this set of attributes will be applied. |
| matching_attributes | [MatchingAttributes](#flyteidl-admin-MatchingAttributes) |  |  |
| org | string |  | Optional, org key applied to the attributes. |







### WorkflowAttributesDeleteRequest {#flyteidl-admin-WorkflowAttributesDeleteRequest}
Request to delete a set matchable workflow attribute override.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id which this set of attributes references. +required |
| domain | string |  | Unique domain id which this set of attributes references. +required |
| workflow | string |  | Workflow name which this set of attributes references. +required |
| resource_type | [MatchableResource](#flyteidl-admin-MatchableResource) |  | Which type of matchable attributes to delete. +required |
| org | string |  | Optional, org key applied to the attributes. |







### WorkflowAttributesDeleteResponse {#flyteidl-admin-WorkflowAttributesDeleteResponse}
Purposefully empty, may be populated in the future.







### WorkflowAttributesGetRequest {#flyteidl-admin-WorkflowAttributesGetRequest}
Request to get an individual workflow attribute override.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id which this set of attributes references. +required |
| domain | string |  | Unique domain id which this set of attributes references. +required |
| workflow | string |  | Workflow name which this set of attributes references. +required |
| resource_type | [MatchableResource](#flyteidl-admin-MatchableResource) |  | Which type of matchable attributes to return. +required |
| org | string |  | Optional, org key applied to the attributes. |







### WorkflowAttributesGetResponse {#flyteidl-admin-WorkflowAttributesGetResponse}
Response to get an individual workflow attribute override.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| attributes | [WorkflowAttributes](#flyteidl-admin-WorkflowAttributes) |  |  |







### WorkflowAttributesUpdateRequest {#flyteidl-admin-WorkflowAttributesUpdateRequest}
Sets custom attributes for a project, domain and workflow combination.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| attributes | [WorkflowAttributes](#flyteidl-admin-WorkflowAttributes) |  |  |







### WorkflowAttributesUpdateResponse {#flyteidl-admin-WorkflowAttributesUpdateResponse}
Purposefully empty, may be populated in the future.
















## flyteidl/admin/event.proto




### EventErrorAlreadyInTerminalState {#flyteidl-admin-EventErrorAlreadyInTerminalState}
Indicates that a sent event was not used to update execution state due to
the referenced execution already being terminated (and therefore ineligible
for further state transitions).



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| current_phase | string |  | +required |







### EventErrorIncompatibleCluster {#flyteidl-admin-EventErrorIncompatibleCluster}
Indicates an event was rejected because it came from a different cluster than
is on record as running the execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cluster | string |  | The cluster which has been recorded as processing the execution. +required |







### EventFailureReason {#flyteidl-admin-EventFailureReason}
Indicates why a sent event was not used to update execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| already_in_terminal_state | [EventErrorAlreadyInTerminalState](#flyteidl-admin-EventErrorAlreadyInTerminalState) |  |  |
| incompatible_cluster | [EventErrorIncompatibleCluster](#flyteidl-admin-EventErrorIncompatibleCluster) |  |  |







### NodeExecutionEventRequest {#flyteidl-admin-NodeExecutionEventRequest}
Request to send a notification that a node execution event has occurred.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | string |  | Unique ID for this request that can be traced between services |
| event | [flyteidl.event.NodeExecutionEvent](#flyteidl-event-NodeExecutionEvent) |  | Details about the event that occurred. |







### NodeExecutionEventResponse {#flyteidl-admin-NodeExecutionEventResponse}
Purposefully empty, may be populated in the future.







### TaskExecutionEventRequest {#flyteidl-admin-TaskExecutionEventRequest}
Request to send a notification that a task execution event has occurred.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | string |  | Unique ID for this request that can be traced between services |
| event | [flyteidl.event.TaskExecutionEvent](#flyteidl-event-TaskExecutionEvent) |  | Details about the event that occurred. |







### TaskExecutionEventResponse {#flyteidl-admin-TaskExecutionEventResponse}
Purposefully empty, may be populated in the future.







### WorkflowExecutionEventRequest {#flyteidl-admin-WorkflowExecutionEventRequest}
Request to send a notification that a workflow execution event has occurred.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_id | string |  | Unique ID for this request that can be traced between services |
| event | [flyteidl.event.WorkflowExecutionEvent](#flyteidl-event-WorkflowExecutionEvent) |  | Details about the event that occurred. |







### WorkflowExecutionEventResponse {#flyteidl-admin-WorkflowExecutionEventResponse}
Purposefully empty, may be populated in the future.
















## flyteidl/admin/matchable_resource.proto




### ClusterResourceAttributes {#flyteidl-admin-ClusterResourceAttributes}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| attributes | [ClusterResourceAttributes.AttributesEntry](#flyteidl-admin-ClusterResourceAttributes-AttributesEntry) | repeated | Custom resource attributes which will be applied in cluster resource creation (e.g. quotas). Map keys are the *case-sensitive* names of variables in templatized resource files. Map values should be the custom values which get substituted during resource creation. |







### ClusterResourceAttributes.AttributesEntry {#flyteidl-admin-ClusterResourceAttributes-AttributesEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### ExecutionClusterLabel {#flyteidl-admin-ExecutionClusterLabel}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | string |  | Label value to determine where the execution will be run |







### ExecutionQueueAttributes {#flyteidl-admin-ExecutionQueueAttributes}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tags | string | repeated | Tags used for assigning execution queues for tasks defined within this project. |







### ListMatchableAttributesRequest {#flyteidl-admin-ListMatchableAttributesRequest}
Request all matching resource attributes for a resource type.
See :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_type | [MatchableResource](#flyteidl-admin-MatchableResource) |  | +required |
| org | string |  | Optional, org filter applied to list project requests. |







### ListMatchableAttributesResponse {#flyteidl-admin-ListMatchableAttributesResponse}
Response for a request for all matching resource attributes for a resource type.
See :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| configurations | [MatchableAttributesConfiguration](#flyteidl-admin-MatchableAttributesConfiguration) | repeated |  |







### MatchableAttributesConfiguration {#flyteidl-admin-MatchableAttributesConfiguration}
Represents a custom set of attributes applied for either a domain (and optional org); a domain and project (and optional org);
or domain, project and workflow name (and optional org).
These are used to override system level defaults for kubernetes cluster resource management,
default execution values, and more all across different levels of specificity.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| attributes | [MatchingAttributes](#flyteidl-admin-MatchingAttributes) |  |  |
| domain | string |  |  |
| project | string |  |  |
| workflow | string |  |  |
| launch_plan | string |  |  |
| org | string |  | Optional, org key applied to the resource. |







### MatchingAttributes {#flyteidl-admin-MatchingAttributes}
Generic container for encapsulating all types of the above attributes messages.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_resource_attributes | [TaskResourceAttributes](#flyteidl-admin-TaskResourceAttributes) |  |  |
| cluster_resource_attributes | [ClusterResourceAttributes](#flyteidl-admin-ClusterResourceAttributes) |  |  |
| execution_queue_attributes | [ExecutionQueueAttributes](#flyteidl-admin-ExecutionQueueAttributes) |  |  |
| execution_cluster_label | [ExecutionClusterLabel](#flyteidl-admin-ExecutionClusterLabel) |  |  |
| quality_of_service | [flyteidl.core.QualityOfService](#flyteidl-core-QualityOfService) |  |  |
| plugin_overrides | [PluginOverrides](#flyteidl-admin-PluginOverrides) |  |  |
| workflow_execution_config | [WorkflowExecutionConfig](#flyteidl-admin-WorkflowExecutionConfig) |  |  |
| cluster_assignment | [ClusterAssignment](#flyteidl-admin-ClusterAssignment) |  |  |







### PluginOverride {#flyteidl-admin-PluginOverride}
This MatchableAttribute configures selecting alternate plugin implementations for a given task type.
In addition to an override implementation a selection of fallbacks can be provided or other modes
for handling cases where the desired plugin override is not enabled in a given Flyte deployment.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_type | string |  | A predefined yet extensible Task type identifier. |
| plugin_id | string | repeated | A set of plugin ids which should handle tasks of this type instead of the default registered plugin. The list will be tried in order until a plugin is found with that id. |
| missing_plugin_behavior | [PluginOverride.MissingPluginBehavior](#flyteidl-admin-PluginOverride-MissingPluginBehavior) |  | Defines the behavior when no plugin from the plugin_id list is not found. |







### PluginOverrides {#flyteidl-admin-PluginOverrides}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| overrides | [PluginOverride](#flyteidl-admin-PluginOverride) | repeated |  |







### TaskResourceAttributes {#flyteidl-admin-TaskResourceAttributes}
Defines task resource defaults and limits that will be applied at task registration.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| defaults | [TaskResourceSpec](#flyteidl-admin-TaskResourceSpec) |  |  |
| limits | [TaskResourceSpec](#flyteidl-admin-TaskResourceSpec) |  |  |







### TaskResourceSpec {#flyteidl-admin-TaskResourceSpec}
Defines a set of overridable task resource attributes set during task registration.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cpu | string |  |  |
| gpu | string |  |  |
| memory | string |  |  |
| storage | string |  |  |
| ephemeral_storage | string |  |  |







### WorkflowExecutionConfig {#flyteidl-admin-WorkflowExecutionConfig}
Adds defaults for customizable workflow-execution specifications and overrides.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| max_parallelism | int32 |  | Can be used to control the number of parallel nodes to run within the workflow. This is useful to achieve fairness. |
| security_context | [flyteidl.core.SecurityContext](#flyteidl-core-SecurityContext) |  | Indicates security context permissions for executions triggered with this matchable attribute. |
| raw_output_data_config | [RawOutputDataConfig](#flyteidl-admin-RawOutputDataConfig) |  | Encapsulates user settings pertaining to offloaded data (i.e. Blobs, Schema, query data, etc.). |
| labels | [Labels](#flyteidl-admin-Labels) |  | Custom labels to be applied to a triggered execution resource. |
| annotations | [Annotations](#flyteidl-admin-Annotations) |  | Custom annotations to be applied to a triggered execution resource. |
| interruptible | google.protobuf.BoolValue |  | Allows for the interruptible flag of a workflow to be overwritten for a single execution. Omitting this field uses the workflow's value as a default. As we need to distinguish between the field not being provided and its default value false, we have to use a wrapper around the bool field. |
| overwrite_cache | bool |  | Allows for all cached values of a workflow and its tasks to be overwritten for a single execution. If enabled, all calculations are performed even if cached results would be available, overwriting the stored data once execution finishes successfully. |
| envs | [Envs](#flyteidl-admin-Envs) |  | Environment variables to be set for the execution. |
| execution_env_assignments | [flyteidl.core.ExecutionEnvAssignment](#flyteidl-core-ExecutionEnvAssignment) | repeated | Execution environment assignments to be set for the execution. |









### MatchableResource {#flyteidl-admin-MatchableResource}
Defines a resource that can be configured by customizable Project-, ProjectDomain- or WorkflowAttributes
based on matching tags.

| Name | Number | Description |
| ---- | ------ | ----------- |
| TASK_RESOURCE | 0 | Applies to customizable task resource requests and limits. |
| CLUSTER_RESOURCE | 1 | Applies to configuring templated kubernetes cluster resources. |
| EXECUTION_QUEUE | 2 | Configures task and dynamic task execution queue assignment. |
| EXECUTION_CLUSTER_LABEL | 3 | Configures the K8s cluster label to be used for execution to be run |
| QUALITY_OF_SERVICE_SPECIFICATION | 4 | Configures default quality of service when undefined in an execution spec. |
| PLUGIN_OVERRIDE | 5 | Selects configurable plugin implementation behavior for a given task type. |
| WORKFLOW_EXECUTION_CONFIG | 6 | Adds defaults for customizable workflow-execution specifications and overrides. |
| CLUSTER_ASSIGNMENT | 7 | Controls how to select an available cluster on which this execution should run. |




### PluginOverride.MissingPluginBehavior {#flyteidl-admin-PluginOverride-MissingPluginBehavior}


| Name | Number | Description |
| ---- | ------ | ----------- |
| FAIL | 0 | By default, if this plugin is not enabled for a Flyte deployment then execution will fail. |
| USE_DEFAULT | 1 | Uses the system-configured default implementation. |











## flyteidl/admin/project_attributes.proto




### ProjectAttributes {#flyteidl-admin-ProjectAttributes}
Defines a set of custom matching attributes at the project level.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id for which this set of attributes will be applied. |
| matching_attributes | [MatchingAttributes](#flyteidl-admin-MatchingAttributes) |  |  |
| org | string |  | Optional, org key applied to the project. |







### ProjectAttributesDeleteRequest {#flyteidl-admin-ProjectAttributesDeleteRequest}
Request to delete a set matchable project level attribute override.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id which this set of attributes references. +required |
| resource_type | [MatchableResource](#flyteidl-admin-MatchableResource) |  | Which type of matchable attributes to delete. +required |
| org | string |  | Optional, org key applied to the project. |







### ProjectAttributesDeleteResponse {#flyteidl-admin-ProjectAttributesDeleteResponse}
Purposefully empty, may be populated in the future.







### ProjectAttributesGetRequest {#flyteidl-admin-ProjectAttributesGetRequest}
Request to get an individual project level attribute override.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id which this set of attributes references. +required |
| resource_type | [MatchableResource](#flyteidl-admin-MatchableResource) |  | Which type of matchable attributes to return. +required |
| org | string |  | Optional, org key applied to the project. |







### ProjectAttributesGetResponse {#flyteidl-admin-ProjectAttributesGetResponse}
Response to get an individual project level attribute override.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| attributes | [ProjectAttributes](#flyteidl-admin-ProjectAttributes) |  |  |







### ProjectAttributesUpdateRequest {#flyteidl-admin-ProjectAttributesUpdateRequest}
Sets custom attributes for a project
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| attributes | [ProjectAttributes](#flyteidl-admin-ProjectAttributes) |  | +required |







### ProjectAttributesUpdateResponse {#flyteidl-admin-ProjectAttributesUpdateResponse}
Purposefully empty, may be populated in the future.
















## flyteidl/admin/version.proto




### GetVersionRequest {#flyteidl-admin-GetVersionRequest}
Empty request for GetVersion







### GetVersionResponse {#flyteidl-admin-GetVersionResponse}
Response for the GetVersion API



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| control_plane_version | [Version](#flyteidl-admin-Version) |  | The control plane version information. FlyteAdmin and related components form the control plane of Flyte |







### Version {#flyteidl-admin-Version}
Provides Version information for a component



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| Build | string |  | Specifies the GIT sha of the build |
| Version | string |  | Version for the build, should follow a semver |
| BuildTime | string |  | Build timestamp |
















## flyteidl/admin/workflow.proto




### CreateWorkflowFailureReason {#flyteidl-admin-CreateWorkflowFailureReason}
When a CreateWorkflowRequest fails due to matching id



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| exists_different_structure | [WorkflowErrorExistsDifferentStructure](#flyteidl-admin-WorkflowErrorExistsDifferentStructure) |  |  |
| exists_identical_structure | [WorkflowErrorExistsIdenticalStructure](#flyteidl-admin-WorkflowErrorExistsIdenticalStructure) |  |  |







### Workflow {#flyteidl-admin-Workflow}
Represents the workflow structure stored in the Admin
A workflow is created by ordering tasks and associating outputs to inputs
in order to produce a directed-acyclic execution graph.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | id represents the unique identifier of the workflow. |
| closure | [WorkflowClosure](#flyteidl-admin-WorkflowClosure) |  | closure encapsulates all the fields that maps to a compiled version of the workflow. |
| short_description | string |  | One-liner overview of the entity. |







### WorkflowClosure {#flyteidl-admin-WorkflowClosure}
A container holding the compiled workflow produced from the WorkflowSpec and additional metadata.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| compiled_workflow | [flyteidl.core.CompiledWorkflowClosure](#flyteidl-core-CompiledWorkflowClosure) |  | Represents the compiled representation of the workflow from the specification provided. |
| created_at | google.protobuf.Timestamp |  | Time at which the workflow was created. |







### WorkflowCreateRequest {#flyteidl-admin-WorkflowCreateRequest}
Represents a request structure to create a revision of a workflow.
See :ref:`ref_flyteidl.admin.Workflow` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | id represents the unique identifier of the workflow. +required |
| spec | [WorkflowSpec](#flyteidl-admin-WorkflowSpec) |  | Represents the specification for workflow. +required |







### WorkflowCreateResponse {#flyteidl-admin-WorkflowCreateResponse}
Purposefully empty, may be populated in the future.







### WorkflowErrorExistsDifferentStructure {#flyteidl-admin-WorkflowErrorExistsDifferentStructure}
The workflow id is already used and the structure is different



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  |  |







### WorkflowErrorExistsIdenticalStructure {#flyteidl-admin-WorkflowErrorExistsIdenticalStructure}
The workflow id is already used with an identical sctructure



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  |  |







### WorkflowList {#flyteidl-admin-WorkflowList}
Represents a list of workflows returned from the admin.
See :ref:`ref_flyteidl.admin.Workflow` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| workflows | [Workflow](#flyteidl-admin-Workflow) | repeated | A list of workflows returned based on the request. |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### WorkflowSpec {#flyteidl-admin-WorkflowSpec}
Represents a structure that encapsulates the specification of the workflow.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| template | [flyteidl.core.WorkflowTemplate](#flyteidl-core-WorkflowTemplate) |  | Template of the task that encapsulates all the metadata of the workflow. |
| sub_workflows | [flyteidl.core.WorkflowTemplate](#flyteidl-core-WorkflowTemplate) | repeated | Workflows that are embedded into other workflows need to be passed alongside the parent workflow to the propeller compiler (since the compiler doesn't have any knowledge of other workflows - ie, it doesn't reach out to Admin to see other registered workflows). In fact, subworkflows do not even need to be registered. |
| description | [DescriptionEntity](#flyteidl-admin-DescriptionEntity) |  | Represents the specification for description entity. |
















## flyteidl/admin/description_entity.proto




### Description {#flyteidl-admin-Description}
Full user description with formatting preserved. This can be rendered
by clients, such as the console or command line tools with in-tact
formatting.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | string |  | long description - no more than 4KB |
| uri | string |  | if the description sizes exceed some threshold we can offload the entire description proto altogether to an external data store, like S3 rather than store inline in the db |
| format | [DescriptionFormat](#flyteidl-admin-DescriptionFormat) |  | Format of the long description |
| icon_link | string |  | Optional link to an icon for the entity |







### DescriptionEntity {#flyteidl-admin-DescriptionEntity}
DescriptionEntity contains detailed description for the task/workflow.
Documentation could provide insight into the algorithms, business use case, etc.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | id represents the unique identifier of the description entity. |
| short_description | string |  | One-liner overview of the entity. |
| long_description | [Description](#flyteidl-admin-Description) |  | Full user description with formatting preserved. |
| source_code | [SourceCode](#flyteidl-admin-SourceCode) |  | Optional link to source code used to define this entity. |
| tags | string | repeated | User-specified tags. These are arbitrary and can be used for searching filtering and discovering tasks. |







### DescriptionEntityList {#flyteidl-admin-DescriptionEntityList}
Represents a list of DescriptionEntities returned from the admin.
See :ref:`ref_flyteidl.admin.DescriptionEntity` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| descriptionEntities | [DescriptionEntity](#flyteidl-admin-DescriptionEntity) | repeated | A list of DescriptionEntities returned based on the request. |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### DescriptionEntityListRequest {#flyteidl-admin-DescriptionEntityListRequest}
Represents a request structure to retrieve a list of DescriptionEntities.
See :ref:`ref_flyteidl.admin.DescriptionEntity` for more details



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_type | [flyteidl.core.ResourceType](#flyteidl-core-ResourceType) |  | Identifies the specific type of resource that this identifier corresponds to. |
| id | [NamedEntityIdentifier](#flyteidl-admin-NamedEntityIdentifier) |  | The identifier for the description entity. +required |
| limit | uint32 |  | Indicates the number of resources to be returned. +required |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. +optional |
| filters | string |  | Indicates a list of filters passed as string. More info on constructing filters : <lt;Link>gt; +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Sort ordering for returned list. +optional |







### SourceCode {#flyteidl-admin-SourceCode}
Link to source code used to define this entity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| link | string |  |  |









### DescriptionFormat {#flyteidl-admin-DescriptionFormat}
The format of the long description

| Name | Number | Description |
| ---- | ------ | ----------- |
| DESCRIPTION_FORMAT_UNKNOWN | 0 |  |
| DESCRIPTION_FORMAT_MARKDOWN | 1 |  |
| DESCRIPTION_FORMAT_HTML | 2 |  |
| DESCRIPTION_FORMAT_RST | 3 | python default documentation - comments is rst |











## flyteidl/admin/project_domain_attributes.proto




### ProjectDomainAttributes {#flyteidl-admin-ProjectDomainAttributes}
Defines a set of custom matching attributes which defines resource defaults for a project and domain.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id for which this set of attributes will be applied. |
| domain | string |  | Unique domain id for which this set of attributes will be applied. |
| matching_attributes | [MatchingAttributes](#flyteidl-admin-MatchingAttributes) |  |  |
| org | string |  | Optional, org key applied to the attributes. |







### ProjectDomainAttributesDeleteRequest {#flyteidl-admin-ProjectDomainAttributesDeleteRequest}
Request to delete a set matchable project domain attribute override.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id which this set of attributes references. +required |
| domain | string |  | Unique domain id which this set of attributes references. +required |
| resource_type | [MatchableResource](#flyteidl-admin-MatchableResource) |  | Which type of matchable attributes to delete. +required |
| org | string |  | Optional, org key applied to the attributes. |







### ProjectDomainAttributesDeleteResponse {#flyteidl-admin-ProjectDomainAttributesDeleteResponse}
Purposefully empty, may be populated in the future.







### ProjectDomainAttributesGetRequest {#flyteidl-admin-ProjectDomainAttributesGetRequest}
Request to get an individual project domain attribute override.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Unique project id which this set of attributes references. +required |
| domain | string |  | Unique domain id which this set of attributes references. +required |
| resource_type | [MatchableResource](#flyteidl-admin-MatchableResource) |  | Which type of matchable attributes to return. +required |
| org | string |  | Optional, org key applied to the attributes. |







### ProjectDomainAttributesGetResponse {#flyteidl-admin-ProjectDomainAttributesGetResponse}
Response to get an individual project domain attribute override.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| attributes | [ProjectDomainAttributes](#flyteidl-admin-ProjectDomainAttributes) |  |  |







### ProjectDomainAttributesUpdateRequest {#flyteidl-admin-ProjectDomainAttributesUpdateRequest}
Sets custom attributes for a project-domain combination.
For more info on matchable attributes, see :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration`



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| attributes | [ProjectDomainAttributes](#flyteidl-admin-ProjectDomainAttributes) |  | +required |







### ProjectDomainAttributesUpdateResponse {#flyteidl-admin-ProjectDomainAttributesUpdateResponse}
Purposefully empty, may be populated in the future.
















## flyteidl/admin/agent.proto




### Agent {#flyteidl-admin-Agent}
A message containing the agent metadata.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | Name is the developer-assigned name of the agent. |
| supported_task_types | string | repeated | **Deprecated.** SupportedTaskTypes are the types of the tasks that the agent can handle. |
| is_sync | bool |  | IsSync indicates whether this agent is a sync agent. Sync agents are expected to return their results synchronously when called by propeller. Given that sync agents can affect the performance of the system, it's important to enforce strict timeout policies. An Async agent, on the other hand, is required to be able to identify jobs by an identifier and query for job statuses as jobs progress. |
| supported_task_categories | [TaskCategory](#flyteidl-admin-TaskCategory) | repeated | Supported_task_categories are the categories of the tasks that the agent can handle. |







### AgentError {#flyteidl-admin-AgentError}
Error message to propagate detailed errors from agent executions to the execution
engine.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | string |  | A simplified code for errors, so that we can provide a glossary of all possible errors. |
| kind | [AgentError.Kind](#flyteidl-admin-AgentError-Kind) |  | An abstract error kind for this error. Defaults to Non_Recoverable if not specified. |
| origin | [flyteidl.core.ExecutionError.ErrorKind](#flyteidl-core-ExecutionError-ErrorKind) |  | Defines the origin of the error (system, user, unknown). |







### CreateRequestHeader {#flyteidl-admin-CreateRequestHeader}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| template | [flyteidl.core.TaskTemplate](#flyteidl-core-TaskTemplate) |  | Template of the task that encapsulates all the metadata of the task. |
| output_prefix | string |  | Prefix for where task output data will be written. (e.g. s3://my-bucket/randomstring) |
| task_execution_metadata | [TaskExecutionMetadata](#flyteidl-admin-TaskExecutionMetadata) |  | subset of runtime task execution metadata. |
| max_dataset_size_bytes | int64 |  | MaxDatasetSizeBytes is the maximum size of the dataset that can be generated by the task. |







### CreateTaskRequest {#flyteidl-admin-CreateTaskRequest}
Represents a request structure to create task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | The inputs required to start the execution. All required inputs must be included in this map. If not required and not provided, defaults apply. +optional |
| template | [flyteidl.core.TaskTemplate](#flyteidl-core-TaskTemplate) |  | Template of the task that encapsulates all the metadata of the task. |
| output_prefix | string |  | Prefix for where task output data will be written. (e.g. s3://my-bucket/randomstring) |
| task_execution_metadata | [TaskExecutionMetadata](#flyteidl-admin-TaskExecutionMetadata) |  | subset of runtime task execution metadata. |







### CreateTaskResponse {#flyteidl-admin-CreateTaskResponse}
Represents a create response structure.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_meta | bytes |  | ResourceMeta is created by the agent. It could be a string (jobId) or a dict (more complex metadata). |







### DeleteTaskRequest {#flyteidl-admin-DeleteTaskRequest}
A message used to delete a task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_type | string |  | **Deprecated.** A predefined yet extensible Task type identifier. |
| resource_meta | bytes |  | Metadata about the resource to be pass to the agent. |
| task_category | [TaskCategory](#flyteidl-admin-TaskCategory) |  | A predefined yet extensible Task type identifier. |







### DeleteTaskResponse {#flyteidl-admin-DeleteTaskResponse}
Response to delete a task.







### ExecuteTaskSyncRequest {#flyteidl-admin-ExecuteTaskSyncRequest}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [CreateRequestHeader](#flyteidl-admin-CreateRequestHeader) |  |  |
| inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  |  |







### ExecuteTaskSyncResponse {#flyteidl-admin-ExecuteTaskSyncResponse}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [ExecuteTaskSyncResponseHeader](#flyteidl-admin-ExecuteTaskSyncResponseHeader) |  |  |
| outputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  |  |







### ExecuteTaskSyncResponseHeader {#flyteidl-admin-ExecuteTaskSyncResponseHeader}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource | [Resource](#flyteidl-admin-Resource) |  |  |







### GetAgentRequest {#flyteidl-admin-GetAgentRequest}
A request to get an agent.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | The name of the agent. |







### GetAgentResponse {#flyteidl-admin-GetAgentResponse}
A response containing an agent.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| agent | [Agent](#flyteidl-admin-Agent) |  |  |







### GetTaskLogsRequest {#flyteidl-admin-GetTaskLogsRequest}
A request to get the log from a task execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_type | string |  | **Deprecated.** A predefined yet extensible Task type identifier. |
| resource_meta | bytes |  | Metadata is created by the agent. It could be a string (jobId) or a dict (more complex metadata). |
| lines | uint64 |  | Number of lines to return. |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |
| task_category | [TaskCategory](#flyteidl-admin-TaskCategory) |  | A predefined yet extensible Task type identifier. |







### GetTaskLogsResponse {#flyteidl-admin-GetTaskLogsResponse}
A response containing the logs for a task execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [GetTaskLogsResponseHeader](#flyteidl-admin-GetTaskLogsResponseHeader) |  |  |
| body | [GetTaskLogsResponseBody](#flyteidl-admin-GetTaskLogsResponseBody) |  |  |







### GetTaskLogsResponseBody {#flyteidl-admin-GetTaskLogsResponseBody}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| results | string | repeated | **Deprecated.** The execution log results. |
| structured_lines | [LogLine](#flyteidl-admin-LogLine) | repeated | Each line is separated by either CRLF, CR or LF, which are included at the ends of the lines. This lets clients know whether log emitter wanted to overwrite the previous line (LF) or append a new line (CRLF). |







### GetTaskLogsResponseHeader {#flyteidl-admin-GetTaskLogsResponseHeader}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### GetTaskMetricsRequest {#flyteidl-admin-GetTaskMetricsRequest}
A request to get the metrics from a task execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_type | string |  | **Deprecated.** A predefined yet extensible Task type identifier. |
| resource_meta | bytes |  | Metadata is created by the agent. It could be a string (jobId) or a dict (more complex metadata). |
| queries | string | repeated | The metrics to query. If empty, will return a default set of metrics. e.g. EXECUTION_METRIC_USED_CPU_AVG or EXECUTION_METRIC_USED_MEMORY_BYTES_AVG |
| start_time | google.protobuf.Timestamp |  | Start timestamp, inclusive. |
| end_time | google.protobuf.Timestamp |  | End timestamp, inclusive.. |
| step | google.protobuf.Duration |  | Query resolution step width in duration format or float number of seconds. |
| task_category | [TaskCategory](#flyteidl-admin-TaskCategory) |  | A predefined yet extensible Task type identifier. |







### GetTaskMetricsResponse {#flyteidl-admin-GetTaskMetricsResponse}
A response containing a list of metrics for a task execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| results | [flyteidl.core.ExecutionMetricResult](#flyteidl-core-ExecutionMetricResult) | repeated | The execution metric results. |







### GetTaskRequest {#flyteidl-admin-GetTaskRequest}
A message used to fetch a job resource from flyte agent server.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_type | string |  | **Deprecated.** A predefined yet extensible Task type identifier. |
| resource_meta | bytes |  | Metadata about the resource to be pass to the agent. |
| task_category | [TaskCategory](#flyteidl-admin-TaskCategory) |  | A predefined yet extensible Task type identifier. |
| output_prefix | string |  | Prefix for where task output data will be written. (e.g. s3://my-bucket/randomstring) |







### GetTaskResponse {#flyteidl-admin-GetTaskResponse}
Response to get an individual task resource.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource | [Resource](#flyteidl-admin-Resource) |  |  |







### ListAgentsRequest {#flyteidl-admin-ListAgentsRequest}
A request to list all agents.







### ListAgentsResponse {#flyteidl-admin-ListAgentsResponse}
A response containing a list of agents.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| agents | [Agent](#flyteidl-admin-Agent) | repeated |  |







### LogLine {#flyteidl-admin-LogLine}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | google.protobuf.Timestamp |  |  |
| message | string |  | Each line is separated by either CRLF, CR or LF, which are included at the ends of the lines. This lets clients know whether log emitter wanted to overwrite the previous line (LF) or append a new line (CRLF). |
| originator | [LogLineOriginator](#flyteidl-admin-LogLineOriginator) |  |  |







### Resource {#flyteidl-admin-Resource}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [State](#flyteidl-admin-State) |  | **Deprecated.** DEPRECATED. The state of the execution is used to control its visibility in the UI/CLI. |
| outputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | The outputs of the execution. It's typically used by sql task. Agent service will create a Structured dataset pointing to the query result table. +optional |
| message | string |  | A descriptive message for the current state. e.g. waiting for cluster. |
| log_links | [flyteidl.core.TaskLog](#flyteidl-core-TaskLog) | repeated | log information for the task execution. |
| phase | [flyteidl.core.TaskExecution.Phase](#flyteidl-core-TaskExecution-Phase) |  | The phase of the execution is used to determine the phase of the plugin's execution. |
| custom_info | google.protobuf.Struct |  | Custom data specific to the agent. |
| agent_error | [AgentError](#flyteidl-admin-AgentError) |  | The error raised during execution |







### TaskCategory {#flyteidl-admin-TaskCategory}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | The name of the task type. |
| version | int32 |  | The version of the task type. |







### TaskExecutionMetadata {#flyteidl-admin-TaskExecutionMetadata}
Represents a subset of runtime task execution metadata that are relevant to external plugins.

ID of the task execution



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_execution_id | [flyteidl.core.TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  |  |
| namespace | string |  | k8s namespace where the task is executed in |
| labels | [TaskExecutionMetadata.LabelsEntry](#flyteidl-admin-TaskExecutionMetadata-LabelsEntry) | repeated | Labels attached to the task execution |
| annotations | [TaskExecutionMetadata.AnnotationsEntry](#flyteidl-admin-TaskExecutionMetadata-AnnotationsEntry) | repeated | Annotations attached to the task execution |
| k8s_service_account | string |  | k8s service account associated with the task execution |
| environment_variables | [TaskExecutionMetadata.EnvironmentVariablesEntry](#flyteidl-admin-TaskExecutionMetadata-EnvironmentVariablesEntry) | repeated | Environment variables attached to the task execution |
| max_attempts | int32 |  | Represents the maximum number of attempts allowed for a task. If a task fails, it can be retried up to this maximum number of attempts. |
| interruptible | bool |  | Indicates whether the task execution can be interrupted. If set to true, the task can be stopped before completion. |
| interruptible_failure_threshold | int32 |  | Specifies the threshold for failure count at which the interruptible property will take effect. If the number of consecutive task failures exceeds this threshold, interruptible behavior will be activated. |
| overrides | [flyteidl.core.TaskNodeOverrides](#flyteidl-core-TaskNodeOverrides) |  | Overrides for specific properties of the task node. These overrides can be used to customize the behavior of the task node. |
| identity | [flyteidl.core.Identity](#flyteidl-core-Identity) |  | Identity of user running this task execution |







### TaskExecutionMetadata.AnnotationsEntry {#flyteidl-admin-TaskExecutionMetadata-AnnotationsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### TaskExecutionMetadata.EnvironmentVariablesEntry {#flyteidl-admin-TaskExecutionMetadata-EnvironmentVariablesEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### TaskExecutionMetadata.LabelsEntry {#flyteidl-admin-TaskExecutionMetadata-LabelsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |









### AgentError.Kind {#flyteidl-admin-AgentError-Kind}
Defines a generic error type that dictates the behavior of the retry strategy.

| Name | Number | Description |
| ---- | ------ | ----------- |
| NON_RECOVERABLE | 0 |  |
| RECOVERABLE | 1 |  |




### LogLineOriginator {#flyteidl-admin-LogLineOriginator}


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 | The originator of the log line is unknown. |
| USER | 1 | The originator of the log line is the user application. |
| SYSTEM | 2 | The originator of the log line is the system. |




### State {#flyteidl-admin-State}
The state of the execution is used to control its visibility in the UI/CLI.

| Name | Number | Description |
| ---- | ------ | ----------- |
| RETRYABLE_FAILURE | 0 |  |
| PERMANENT_FAILURE | 1 |  |
| PENDING | 2 |  |
| RUNNING | 3 |  |
| SUCCEEDED | 4 |  |











## flyteidl/admin/common.proto




### Annotations {#flyteidl-admin-Annotations}
Annotation values to be applied to an execution resource.
In the future a mode (e.g. OVERRIDE, APPEND, etc) can be defined
to specify how to merge annotations defined at registration and execution time.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [Annotations.ValuesEntry](#flyteidl-admin-Annotations-ValuesEntry) | repeated | Map of custom annotations to be applied to the execution resource. |







### Annotations.ValuesEntry {#flyteidl-admin-Annotations-ValuesEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### AuthRole {#flyteidl-admin-AuthRole}
Defines permissions associated with executions created by this launch plan spec.
Use either of these roles when they have permissions required by your workflow execution.
Deprecated.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| assumable_iam_role | string |  | Defines an optional iam role which will be used for tasks run in executions created with this launch plan. |
| kubernetes_service_account | string |  | Defines an optional kubernetes service account which will be used for tasks run in executions created with this launch plan. |







### EmailNotification {#flyteidl-admin-EmailNotification}
Defines an email notification specification.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipients_email | string | repeated | The list of email addresses recipients for this notification. +required |
| template | string |  | The template to use for this notification. +optional |







### Envs {#flyteidl-admin-Envs}
Environment variable values to be applied to an execution resource.
In the future a mode (e.g. OVERRIDE, APPEND, etc) can be defined
to specify how to merge environment variables defined at registration and execution time.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [flyteidl.core.KeyValuePair](#flyteidl-core-KeyValuePair) | repeated | Map of custom environment variables to be applied to the execution resource. |







### FlyteURLs {#flyteidl-admin-FlyteURLs}
These URLs are returned as part of node and task execution data requests.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inputs | string |  |  |
| outputs | string |  |  |
| deck | string |  |  |







### Labels {#flyteidl-admin-Labels}
Label values to be applied to an execution resource.
In the future a mode (e.g. OVERRIDE, APPEND, etc) can be defined
to specify how to merge labels defined at registration and execution time.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [Labels.ValuesEntry](#flyteidl-admin-Labels-ValuesEntry) | repeated | Map of custom labels to be applied to the execution resource. |







### Labels.ValuesEntry {#flyteidl-admin-Labels-ValuesEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### NamedEntity {#flyteidl-admin-NamedEntity}
Encapsulates information common to a NamedEntity, a Flyte resource such as a task,
workflow or launch plan. A NamedEntity is exclusively identified by its resource type
and identifier.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_type | [flyteidl.core.ResourceType](#flyteidl-core-ResourceType) |  | Resource type of the named entity. One of Task, Workflow or LaunchPlan. |
| id | [NamedEntityIdentifier](#flyteidl-admin-NamedEntityIdentifier) |  |  |
| metadata | [NamedEntityMetadata](#flyteidl-admin-NamedEntityMetadata) |  | Additional metadata around a named entity. |







### NamedEntityGetRequest {#flyteidl-admin-NamedEntityGetRequest}
A request to retrieve the metadata associated with a NamedEntityIdentifier



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_type | [flyteidl.core.ResourceType](#flyteidl-core-ResourceType) |  | Resource type of the metadata to get. One of Task, Workflow or LaunchPlan. +required |
| id | [NamedEntityIdentifier](#flyteidl-admin-NamedEntityIdentifier) |  | The identifier for the named entity for which to fetch metadata. +required |







### NamedEntityIdentifier {#flyteidl-admin-NamedEntityIdentifier}
Encapsulation of fields that identifies a Flyte resource.
A Flyte resource can be a task, workflow or launch plan.
A resource can internally have multiple versions and is uniquely identified
by project, domain, and name.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Name of the project the resource belongs to. |
| domain | string |  | Name of the domain the resource belongs to. A domain can be considered as a subset within a specific project. |
| name | string |  | User provided value for the resource. The combination of project + domain + name uniquely identifies the resource. +optional - in certain contexts - like 'List API', 'Launch plans' |
| org | string |  | Optional, org key applied to the resource. |







### NamedEntityIdentifierList {#flyteidl-admin-NamedEntityIdentifierList}
Represents a list of NamedEntityIdentifiers.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| entities | [NamedEntityIdentifier](#flyteidl-admin-NamedEntityIdentifier) | repeated | A list of identifiers. |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### NamedEntityIdentifierListRequest {#flyteidl-admin-NamedEntityIdentifierListRequest}
Represents a request structure to list NamedEntityIdentifiers.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Name of the project that contains the identifiers. +required |
| domain | string |  | Name of the domain the identifiers belongs to within the project. +required |
| limit | uint32 |  | Indicates the number of resources to be returned. +required |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Specifies how listed entities should be sorted in the response. +optional |
| filters | string |  | Indicates a list of filters passed as string. +optional |
| org | string |  | Optional, org key applied to the resource. |







### NamedEntityList {#flyteidl-admin-NamedEntityList}
Represents a list of NamedEntityIdentifiers.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| entities | [NamedEntity](#flyteidl-admin-NamedEntity) | repeated | A list of NamedEntity objects |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. If there are no more results, this value will be empty. |







### NamedEntityListRequest {#flyteidl-admin-NamedEntityListRequest}
Represents a request structure to list NamedEntity objects



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_type | [flyteidl.core.ResourceType](#flyteidl-core-ResourceType) |  | Resource type of the metadata to query. One of Task, Workflow or LaunchPlan. +required |
| project | string |  | Name of the project that contains the identifiers. +required |
| domain | string |  | Name of the domain the identifiers belongs to within the project. |
| limit | uint32 |  | Indicates the number of resources to be returned. |
| token | string |  | In the case of multiple pages of results, the server-provided token can be used to fetch the next page in a query. +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Specifies how listed entities should be sorted in the response. +optional |
| filters | string |  | Indicates a list of filters passed as string. +optional |
| org | string |  | Optional, org key applied to the resource. |







### NamedEntityMetadata {#flyteidl-admin-NamedEntityMetadata}
Additional metadata around a named entity.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| description | string |  | Common description across all versions of the entity +optional |
| state | [NamedEntityState](#flyteidl-admin-NamedEntityState) |  | Shared state across all version of the entity At this point in time, only workflow entities can have their state archived. |







### NamedEntityUpdateRequest {#flyteidl-admin-NamedEntityUpdateRequest}
Request to set the referenced named entity state to the configured value.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_type | [flyteidl.core.ResourceType](#flyteidl-core-ResourceType) |  | Resource type of the metadata to update +required |
| id | [NamedEntityIdentifier](#flyteidl-admin-NamedEntityIdentifier) |  | Identifier of the metadata to update +required |
| metadata | [NamedEntityMetadata](#flyteidl-admin-NamedEntityMetadata) |  | Metadata object to set as the new value +required |







### NamedEntityUpdateResponse {#flyteidl-admin-NamedEntityUpdateResponse}
Purposefully empty, may be populated in the future.







### Notification {#flyteidl-admin-Notification}
Represents a structure for notifications based on execution status.
The notification content is configured within flyte admin but can be templatized.
Future iterations could expose configuring notifications with custom content.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| phases | [flyteidl.core.WorkflowExecution.Phase](#flyteidl-core-WorkflowExecution-Phase) | repeated | A list of phases to which users can associate the notifications to. +required |
| email | [EmailNotification](#flyteidl-admin-EmailNotification) |  |  |
| pager_duty | [PagerDutyNotification](#flyteidl-admin-PagerDutyNotification) |  |  |
| slack | [SlackNotification](#flyteidl-admin-SlackNotification) |  |  |







### ObjectGetRequest {#flyteidl-admin-ObjectGetRequest}
Shared request structure to fetch a single resource.
Resources include: Task, Workflow, LaunchPlan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | Indicates a unique version of resource. +required |







### PagerDutyNotification {#flyteidl-admin-PagerDutyNotification}
Defines a pager duty notification specification.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipients_email | string | repeated | Currently, PagerDuty notifications leverage email to trigger a notification. +required |
| template | string |  | The template to use for this notification. +optional |







### RawOutputDataConfig {#flyteidl-admin-RawOutputDataConfig}
Encapsulates user settings pertaining to offloaded data (i.e. Blobs, Schema, query data, etc.).
See https://github.com/flyteorg/flyte/issues/211 for more background information.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| output_location_prefix | string |  | Prefix for where offloaded data from user workflows will be written e.g. s3://bucket/key or s3://bucket/ |







### ResourceListRequest {#flyteidl-admin-ResourceListRequest}
Shared request structure to retrieve a list of resources.
Resources include: Task, Workflow, LaunchPlan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [NamedEntityIdentifier](#flyteidl-admin-NamedEntityIdentifier) |  | id represents the unique identifier of the resource. +required |
| limit | uint32 |  | Indicates the number of resources to be returned. +required |
| token | string |  | In the case of multiple pages of results, this server-provided token can be used to fetch the next page in a query. +optional |
| filters | string |  | Indicates a list of filters passed as string. More info on constructing filters : <lt;Link>gt; +optional |
| sort_by | [Sort](#flyteidl-admin-Sort) |  | Sort ordering. +optional |







### SlackNotification {#flyteidl-admin-SlackNotification}
Defines a slack notification specification.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recipients_email | string | repeated | Currently, Slack notifications leverage email to trigger a notification. +required |
| template | string |  | The template to use for this notification. +optional |







### Sort {#flyteidl-admin-Sort}
Specifies sort ordering in a list request.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  | Indicates an attribute to sort the response values. +required |
| direction | [Sort.Direction](#flyteidl-admin-Sort-Direction) |  | Indicates the direction to apply sort key for response values. +optional |







### UrlBlob {#flyteidl-admin-UrlBlob}
Represents a string url and associated metadata used throughout the platform.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| url | string |  | Actual url value. |
| bytes | int64 |  | Represents the size of the file accessible at the above url. |









### NamedEntityState {#flyteidl-admin-NamedEntityState}
The status of the named entity is used to control its visibility in the UI.

| Name | Number | Description |
| ---- | ------ | ----------- |
| NAMED_ENTITY_ACTIVE | 0 | By default, all named entities are considered active and under development. |
| NAMED_ENTITY_ARCHIVED | 1 | Archived named entities are no longer visible in the UI. |
| SYSTEM_GENERATED | 2 | System generated entities that aren't explicitly created or managed by a user. |




### Sort.Direction {#flyteidl-admin-Sort-Direction}


| Name | Number | Description |
| ---- | ------ | ----------- |
| DESCENDING | 0 | By default, fields are sorted in descending order. |
| ASCENDING | 1 |  |











## flyteidl/cacheservice/cacheservice.proto




### CachedOutput {#flyteidl-cacheservice-CachedOutput}
Represents cached output, either as literals or an URI, with associated metadata.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| output_literals | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Output literals |
| output_uri | string |  | URI to output data |
| metadata | [Metadata](#flyteidl-cacheservice-Metadata) |  | Associated metadata |







### DeleteCacheRequest {#flyteidl-cacheservice-DeleteCacheRequest}
Request to delete cached data by key.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  | Cache key |







### DeleteCacheResponse {#flyteidl-cacheservice-DeleteCacheResponse}
Response message of cache deletion operation.

Empty, success indicated by no errors







### GetCacheRequest {#flyteidl-cacheservice-GetCacheRequest}
Request to retrieve cached data by key.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  | Cache key |







### GetCacheResponse {#flyteidl-cacheservice-GetCacheResponse}
Response with cached data for a given key.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| output | [CachedOutput](#flyteidl-cacheservice-CachedOutput) |  | Cached output |







### GetOrExtendReservationRequest {#flyteidl-cacheservice-GetOrExtendReservationRequest}
Request to get or extend a reservation for a cache key



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  | The unique ID for the reservation - same as the cache key |
| owner_id | string |  | The unique ID of the owner for the reservation |
| heartbeat_interval | google.protobuf.Duration |  | Requested reservation extension heartbeat interval |







### GetOrExtendReservationResponse {#flyteidl-cacheservice-GetOrExtendReservationResponse}
Request to get or extend a reservation for a cache key



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reservation | [Reservation](#flyteidl-cacheservice-Reservation) |  | The reservation that was created or extended |







### KeyMapMetadata {#flyteidl-cacheservice-KeyMapMetadata}
Additional metadata as key-value pairs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [KeyMapMetadata.ValuesEntry](#flyteidl-cacheservice-KeyMapMetadata-ValuesEntry) | repeated | Additional metadata as key-value pairs |







### KeyMapMetadata.ValuesEntry {#flyteidl-cacheservice-KeyMapMetadata-ValuesEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### Metadata {#flyteidl-cacheservice-Metadata}
Metadata for cached outputs, including the source identifier and timestamps.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| source_identifier | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | Source task or workflow identifier |
| key_map | [KeyMapMetadata](#flyteidl-cacheservice-KeyMapMetadata) |  | Additional metadata as key-value pairs |
| created_at | google.protobuf.Timestamp |  | Creation timestamp |
| last_updated_at | google.protobuf.Timestamp |  | Last update timestamp |







### PutCacheRequest {#flyteidl-cacheservice-PutCacheRequest}
Request to store/update cached data by key.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  | Cache key |
| output | [CachedOutput](#flyteidl-cacheservice-CachedOutput) |  | Output to cache |
| overwrite | bool |  | Overwrite flag |







### PutCacheResponse {#flyteidl-cacheservice-PutCacheResponse}
Response message of cache store/update operation.

Empty, success indicated by no errors







### ReleaseReservationRequest {#flyteidl-cacheservice-ReleaseReservationRequest}
Request to release the reservation for a cache key



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  | The unique ID for the reservation - same as the cache key |
| owner_id | string |  | The unique ID of the owner for the reservation |







### ReleaseReservationResponse {#flyteidl-cacheservice-ReleaseReservationResponse}
Response message of release reservation operation.

Empty, success indicated by no errors







### Reservation {#flyteidl-cacheservice-Reservation}
A reservation including owner, heartbeat interval, expiration timestamp, and various metadata.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  | The unique ID for the reservation - same as the cache key |
| owner_id | string |  | The unique ID of the owner for the reservation |
| heartbeat_interval | google.protobuf.Duration |  | Requested reservation extension heartbeat interval |
| expires_at | google.protobuf.Timestamp |  | Expiration timestamp of this reservation |













### CacheService {#flyteidl-cacheservice-CacheService}
CacheService defines operations for cache management including retrieval, storage, and deletion of cached task/workflow outputs.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Get | [GetCacheRequest](#flyteidl-cacheservice-GetCacheRequest) | [GetCacheResponse](#flyteidl-cacheservice-GetCacheResponse) | Retrieves cached data by key. |
| Put | [PutCacheRequest](#flyteidl-cacheservice-PutCacheRequest) | [PutCacheResponse](#flyteidl-cacheservice-PutCacheResponse) | Stores or updates cached data by key. |
| Delete | [DeleteCacheRequest](#flyteidl-cacheservice-DeleteCacheRequest) | [DeleteCacheResponse](#flyteidl-cacheservice-DeleteCacheResponse) | Deletes cached data by key. |
| GetOrExtendReservation | [GetOrExtendReservationRequest](#flyteidl-cacheservice-GetOrExtendReservationRequest) | [GetOrExtendReservationResponse](#flyteidl-cacheservice-GetOrExtendReservationResponse) | Get or extend a reservation for a cache key |
| ReleaseReservation | [ReleaseReservationRequest](#flyteidl-cacheservice-ReleaseReservationRequest) | [ReleaseReservationResponse](#flyteidl-cacheservice-ReleaseReservationResponse) | Release the reservation for a cache key |






## flyteidl/service/signal.proto










### SignalService {#flyteidl-service-SignalService}
SignalService defines an RPC Service that may create, update, and retrieve signal(s).

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOrCreateSignal | [.flyteidl.admin.SignalGetOrCreateRequest](#flyteidl-admin-SignalGetOrCreateRequest) | [.flyteidl.admin.Signal](#flyteidl-admin-Signal) | Fetches or creates a :ref:`ref_flyteidl.admin.Signal`. |
| ListSignals | [.flyteidl.admin.SignalListRequest](#flyteidl-admin-SignalListRequest) | [.flyteidl.admin.SignalList](#flyteidl-admin-SignalList) | Fetch a list of :ref:`ref_flyteidl.admin.Signal` definitions. |
| SetSignal | [.flyteidl.admin.SignalSetRequest](#flyteidl-admin-SignalSetRequest) | [.flyteidl.admin.SignalSetResponse](#flyteidl-admin-SignalSetResponse) | Sets the value on a :ref:`ref_flyteidl.admin.Signal` definition |






## flyteidl/service/external_plugin_service.proto




### TaskCreateRequest {#flyteidl-service-TaskCreateRequest}
Represents a request structure to create task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | The inputs required to start the execution. All required inputs must be included in this map. If not required and not provided, defaults apply. +optional |
| template | [flyteidl.core.TaskTemplate](#flyteidl-core-TaskTemplate) |  | Template of the task that encapsulates all the metadata of the task. |
| output_prefix | string |  | Prefix for where task output data will be written. (e.g. s3://my-bucket/randomstring) |







### TaskCreateResponse {#flyteidl-service-TaskCreateResponse}
Represents a create response structure.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| job_id | string |  |  |







### TaskDeleteRequest {#flyteidl-service-TaskDeleteRequest}
A message used to delete a task.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_type | string |  | A predefined yet extensible Task type identifier. |
| job_id | string |  | The unique id identifying the job. |







### TaskDeleteResponse {#flyteidl-service-TaskDeleteResponse}
Response to delete a task.







### TaskGetRequest {#flyteidl-service-TaskGetRequest}
A message used to fetch a job state from backend plugin server.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_type | string |  | A predefined yet extensible Task type identifier. |
| job_id | string |  | The unique id identifying the job. |







### TaskGetResponse {#flyteidl-service-TaskGetResponse}
Response to get an individual task state.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [State](#flyteidl-service-State) |  | The state of the execution is used to control its visibility in the UI/CLI. |
| outputs | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | The outputs of the execution. It's typically used by sql task. Flyteplugins service will create a Structured dataset pointing to the query result table. +optional |









### State {#flyteidl-service-State}
The state of the execution is used to control its visibility in the UI/CLI.

| Name | Number | Description |
| ---- | ------ | ----------- |
| RETRYABLE_FAILURE | 0 |  |
| PERMANENT_FAILURE | 1 |  |
| PENDING | 2 |  |
| RUNNING | 3 |  |
| SUCCEEDED | 4 |  |








### ExternalPluginService {#flyteidl-service-ExternalPluginService}
ExternalPluginService defines an RPC Service that allows propeller to send the request to the backend plugin server.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| CreateTask | [TaskCreateRequest](#flyteidl-service-TaskCreateRequest) | [TaskCreateResponse](#flyteidl-service-TaskCreateResponse) | Send a task create request to the backend plugin server. |
| GetTask | [TaskGetRequest](#flyteidl-service-TaskGetRequest) | [TaskGetResponse](#flyteidl-service-TaskGetResponse) | Get job status. |
| DeleteTask | [TaskDeleteRequest](#flyteidl-service-TaskDeleteRequest) | [TaskDeleteResponse](#flyteidl-service-TaskDeleteResponse) | Delete the task resource. |






## flyteidl/service/dataproxy.proto




### CreateDownloadLinkRequest {#flyteidl-service-CreateDownloadLinkRequest}
CreateDownloadLinkRequest defines the request parameters to create a download link (signed url)



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact_type | [ArtifactType](#flyteidl-service-ArtifactType) |  | ArtifactType of the artifact requested. |
| expires_in | google.protobuf.Duration |  | ExpiresIn defines a requested expiration duration for the generated url. The request will be rejected if this exceeds the platform allowed max. +optional. The default value comes from a global config. |
| node_execution_id | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | NodeId is the unique identifier for the node execution. For a task node, this will retrieve the output of the most recent attempt of the task. |







### CreateDownloadLinkResponse {#flyteidl-service-CreateDownloadLinkResponse}
CreateDownloadLinkResponse defines the response for the generated links



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signed_url | string | repeated | **Deprecated.** SignedUrl specifies the url to use to download content from (e.g. https://my-bucket.s3.amazonaws.com/randomstring/suffix.tar?X-...) |
| expires_at | google.protobuf.Timestamp |  | **Deprecated.** ExpiresAt defines when will the signed URL expire. |
| pre_signed_urls | [PreSignedURLs](#flyteidl-service-PreSignedURLs) |  | New wrapper object containing the signed urls and expiration time |







### CreateDownloadLocationRequest {#flyteidl-service-CreateDownloadLocationRequest}
CreateDownloadLocationRequest specified request for the CreateDownloadLocation API.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| native_url | string |  | NativeUrl specifies the url in the format of the configured storage provider (e.g. s3://my-bucket/randomstring/suffix.tar) |
| expires_in | google.protobuf.Duration |  | ExpiresIn defines a requested expiration duration for the generated url. The request will be rejected if this exceeds the platform allowed max. +optional. The default value comes from a global config. |







### CreateDownloadLocationResponse {#flyteidl-service-CreateDownloadLocationResponse}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signed_url | string |  | SignedUrl specifies the url to use to download content from (e.g. https://my-bucket.s3.amazonaws.com/randomstring/suffix.tar?X-...) |
| expires_at | google.protobuf.Timestamp |  | ExpiresAt defines when will the signed URL expires. |







### CreateUploadLocationRequest {#flyteidl-service-CreateUploadLocationRequest}
CreateUploadLocationRequest specified request for the CreateUploadLocation API.
The implementation in data proxy service will create the s3 location with some server side configured prefixes,
and then:
  - project/domain/(a deterministic str representation of the content_md5)/filename (if present); OR
  - project/domain/filename_root (if present)/filename (if present).



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | Project to create the upload location for +required |
| domain | string |  | Domain to create the upload location for. +required |
| filename | string |  | Filename specifies a desired suffix for the generated location. E.g. `file.py` or `pre/fix/file.zip`. +optional. By default, the service will generate a consistent name based on the provided parameters. |
| expires_in | google.protobuf.Duration |  | ExpiresIn defines a requested expiration duration for the generated url. The request will be rejected if this exceeds the platform allowed max. +optional. The default value comes from a global config. |
| content_md5 | bytes |  | ContentMD5 restricts the upload location to the specific MD5 provided. The ContentMD5 will also appear in the generated path. +required |
| filename_root | string |  | If present, data proxy will use this string in lieu of the md5 hash in the path. When the filename is also included this makes the upload location deterministic. The native url will still be prefixed by the upload location prefix in data proxy config. This option is useful when uploading multiple files. +optional |
| add_content_md5_metadata | bool |  | If true, the data proxy will add content_md5 to the metadata to the signed URL and it will force clients to add this metadata to the object. This make sure dataproxy is backward compatible with the old flytekit. |
| org | string |  | Optional, org key applied to the resource. |







### CreateUploadLocationResponse {#flyteidl-service-CreateUploadLocationResponse}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signed_url | string |  | SignedUrl specifies the url to use to upload content to (e.g. https://my-bucket.s3.amazonaws.com/randomstring/suffix.tar?X-...) |
| native_url | string |  | NativeUrl specifies the url in the format of the configured storage provider (e.g. s3://my-bucket/randomstring/suffix.tar) |
| expires_at | google.protobuf.Timestamp |  | ExpiresAt defines when will the signed URL expires. |
| headers | [CreateUploadLocationResponse.HeadersEntry](#flyteidl-service-CreateUploadLocationResponse-HeadersEntry) | repeated | Data proxy generates these headers for client, and they have to add these headers to the request when uploading the file. |







### CreateUploadLocationResponse.HeadersEntry {#flyteidl-service-CreateUploadLocationResponse-HeadersEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### GetDataRequest {#flyteidl-service-GetDataRequest}
General request artifact to retrieve data from a Flyte artifact url.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| flyte_url | string |  | A unique identifier in the form of flyte://<lt;something>gt; that uniquely, for a given Flyte backend, identifies a Flyte artifact ([i]nput, [o]output, flyte [d]eck, etc.). e.g. flyte://v1/proj/development/execid/n2/0/i (for 0th task execution attempt input) flyte://v1/proj/development/execid/n2/i (for node execution input) flyte://v1/proj/development/execid/n2/o/o3 (the o3 output of the second node) |







### GetDataResponse {#flyteidl-service-GetDataResponse}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| literal_map | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | literal map data will be returned |
| pre_signed_urls | [PreSignedURLs](#flyteidl-service-PreSignedURLs) |  | Flyte deck html will be returned as a signed url users can download |
| literal | [flyteidl.core.Literal](#flyteidl-core-Literal) |  | Single literal will be returned. This is returned when the user/url requests a specific output or input by name. See the o3 example above. |







### PreSignedURLs {#flyteidl-service-PreSignedURLs}
Wrapper object since the message is shared across this and the GetDataResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signed_url | string | repeated | SignedUrl specifies the url to use to download content from (e.g. https://my-bucket.s3.amazonaws.com/randomstring/suffix.tar?X-...) |
| expires_at | google.protobuf.Timestamp |  | ExpiresAt defines when will the signed URL expire. |









### ArtifactType {#flyteidl-service-ArtifactType}
ArtifactType

| Name | Number | Description |
| ---- | ------ | ----------- |
| ARTIFACT_TYPE_UNDEFINED | 0 | ARTIFACT_TYPE_UNDEFINED is the default, often invalid, value for the enum. |
| ARTIFACT_TYPE_DECK | 1 | ARTIFACT_TYPE_DECK refers to the deck html file optionally generated after a task, a workflow or a launch plan finishes executing. |








### DataProxyService {#flyteidl-service-DataProxyService}
DataProxyService defines an RPC Service that allows access to user-data in a controlled manner.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| CreateUploadLocation | [CreateUploadLocationRequest](#flyteidl-service-CreateUploadLocationRequest) | [CreateUploadLocationResponse](#flyteidl-service-CreateUploadLocationResponse) | CreateUploadLocation creates a signed url to upload artifacts to for a given project/domain. |
| CreateDownloadLocation | [CreateDownloadLocationRequest](#flyteidl-service-CreateDownloadLocationRequest) | [CreateDownloadLocationResponse](#flyteidl-service-CreateDownloadLocationResponse) | CreateDownloadLocation creates a signed url to download artifacts. |
| CreateDownloadLink | [CreateDownloadLinkRequest](#flyteidl-service-CreateDownloadLinkRequest) | [CreateDownloadLinkResponse](#flyteidl-service-CreateDownloadLinkResponse) | CreateDownloadLocation creates a signed url to download artifacts. |
| GetData | [GetDataRequest](#flyteidl-service-GetDataRequest) | [GetDataResponse](#flyteidl-service-GetDataResponse) |  |






## flyteidl/service/identity.proto




### UserInfoRequest {#flyteidl-service-UserInfoRequest}








### UserInfoResponse {#flyteidl-service-UserInfoResponse}
See the OpenID Connect spec at https://openid.net/specs/openid-connect-core-1_0.html#UserInfoResponse for more information.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| subject | string |  | Locally unique and never reassigned identifier within the Issuer for the End-User, which is intended to be consumed by the Client. |
| name | string |  | Full name |
| preferred_username | string |  | Shorthand name by which the End-User wishes to be referred to |
| given_name | string |  | Given name(s) or first name(s) |
| family_name | string |  | Surname(s) or last name(s) |
| email | string |  | Preferred e-mail address |
| picture | string |  | Profile picture URL |
| additional_claims | google.protobuf.Struct |  | Additional claims |













### IdentityService {#flyteidl-service-IdentityService}
IdentityService defines an RPC Service that interacts with user/app identities.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| UserInfo | [UserInfoRequest](#flyteidl-service-UserInfoRequest) | [UserInfoResponse](#flyteidl-service-UserInfoResponse) | Retrieves user information about the currently logged in user. |






## flyteidl/service/auth.proto




### OAuth2MetadataRequest {#flyteidl-service-OAuth2MetadataRequest}








### OAuth2MetadataResponse {#flyteidl-service-OAuth2MetadataResponse}
OAuth2MetadataResponse defines an RFC-Compliant response for /.well-known/oauth-authorization-server metadata
as defined in https://tools.ietf.org/html/rfc8414



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| issuer | string |  | Defines the issuer string in all JWT tokens this server issues. The issuer can be admin itself or an external issuer. |
| authorization_endpoint | string |  | URL of the authorization server's authorization endpoint [RFC6749]. This is REQUIRED unless no grant types are supported that use the authorization endpoint. |
| token_endpoint | string |  | URL of the authorization server's token endpoint [RFC6749]. |
| response_types_supported | string | repeated | Array containing a list of the OAuth 2.0 response_type values that this authorization server supports. |
| scopes_supported | string | repeated | JSON array containing a list of the OAuth 2.0 [RFC6749] scope values that this authorization server supports. |
| token_endpoint_auth_methods_supported | string | repeated | JSON array containing a list of client authentication methods supported by this token endpoint. |
| jwks_uri | string |  | URL of the authorization server's JWK Set [JWK] document. The referenced document contains the signing key(s) the client uses to validate signatures from the authorization server. |
| code_challenge_methods_supported | string | repeated | JSON array containing a list of Proof Key for Code Exchange (PKCE) [RFC7636] code challenge methods supported by this authorization server. |
| grant_types_supported | string | repeated | JSON array containing a list of the OAuth 2.0 grant type values that this authorization server supports. |
| device_authorization_endpoint | string |  | URL of the authorization server's device authorization endpoint, as defined in Section 3.1 of [RFC8628] |







### PublicClientAuthConfigRequest {#flyteidl-service-PublicClientAuthConfigRequest}








### PublicClientAuthConfigResponse {#flyteidl-service-PublicClientAuthConfigResponse}
FlyteClientResponse encapsulates public information that flyte clients (CLIs... etc.) can use to authenticate users.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| client_id | string |  | client_id to use when initiating OAuth2 authorization requests. |
| redirect_uri | string |  | redirect uri to use when initiating OAuth2 authorization requests. |
| scopes | string | repeated | scopes to request when initiating OAuth2 authorization requests. |
| authorization_metadata_key | string |  | Authorization Header to use when passing Access Tokens to the server. If not provided, the client should use the default http `Authorization` header. |
| service_http_endpoint | string |  | ServiceHttpEndpoint points to the http endpoint for the backend. If empty, clients can assume the endpoint used to configure the gRPC connection can be used for the http one respecting the insecure flag to choose between SSL or no SSL connections. |
| audience | string |  | audience to use when initiating OAuth2 authorization requests. |













### AuthMetadataService {#flyteidl-service-AuthMetadataService}
The following defines an RPC service that is also served over HTTP via grpc-gateway.
Standard response codes for both are defined here: https://github.com/grpc-ecosystem/grpc-gateway/blob/master/runtime/errors.go
RPCs defined in this service must be anonymously accessible.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOAuth2Metadata | [OAuth2MetadataRequest](#flyteidl-service-OAuth2MetadataRequest) | [OAuth2MetadataResponse](#flyteidl-service-OAuth2MetadataResponse) | Anonymously accessible. Retrieves local or external oauth authorization server metadata. |
| GetPublicClientConfig | [PublicClientAuthConfigRequest](#flyteidl-service-PublicClientAuthConfigRequest) | [PublicClientAuthConfigResponse](#flyteidl-service-PublicClientAuthConfigResponse) | Anonymously accessible. Retrieves the client information clients should use when initiating OAuth2 authorization requests. |






## flyteidl/service/agent.proto










### AgentMetadataService {#flyteidl-service-AgentMetadataService}
AgentMetadataService defines an RPC service that is also served over HTTP via grpc-gateway.
This service allows propeller or users to get the metadata of agents.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetAgent | [.flyteidl.admin.GetAgentRequest](#flyteidl-admin-GetAgentRequest) | [.flyteidl.admin.GetAgentResponse](#flyteidl-admin-GetAgentResponse) | Fetch a :ref:`ref_flyteidl.admin.Agent` definition. |
| ListAgents | [.flyteidl.admin.ListAgentsRequest](#flyteidl-admin-ListAgentsRequest) | [.flyteidl.admin.ListAgentsResponse](#flyteidl-admin-ListAgentsResponse) | Fetch a list of :ref:`ref_flyteidl.admin.Agent` definitions. |



### AsyncAgentService {#flyteidl-service-AsyncAgentService}
AsyncAgentService defines an RPC Service that allows propeller to send the request to the agent server asynchronously.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| CreateTask | [.flyteidl.admin.CreateTaskRequest](#flyteidl-admin-CreateTaskRequest) | [.flyteidl.admin.CreateTaskResponse](#flyteidl-admin-CreateTaskResponse) | CreateTask sends a task create request to the agent service. |
| GetTask | [.flyteidl.admin.GetTaskRequest](#flyteidl-admin-GetTaskRequest) | [.flyteidl.admin.GetTaskResponse](#flyteidl-admin-GetTaskResponse) | Get job status. |
| DeleteTask | [.flyteidl.admin.DeleteTaskRequest](#flyteidl-admin-DeleteTaskRequest) | [.flyteidl.admin.DeleteTaskResponse](#flyteidl-admin-DeleteTaskResponse) | Delete the task resource. |
| GetTaskMetrics | [.flyteidl.admin.GetTaskMetricsRequest](#flyteidl-admin-GetTaskMetricsRequest) | [.flyteidl.admin.GetTaskMetricsResponse](#flyteidl-admin-GetTaskMetricsResponse) | GetTaskMetrics returns one or more task execution metrics, if available.

Errors include * OutOfRange if metrics are not available for the specified task time range * various other errors |
| GetTaskLogs | [.flyteidl.admin.GetTaskLogsRequest](#flyteidl-admin-GetTaskLogsRequest) | [.flyteidl.admin.GetTaskLogsResponse](#flyteidl-admin-GetTaskLogsResponse) stream | GetTaskLogs returns task execution logs, if available. |



### SyncAgentService {#flyteidl-service-SyncAgentService}
SyncAgentService defines an RPC Service that allows propeller to send the request to the agent server synchronously.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ExecuteTaskSync | [.flyteidl.admin.ExecuteTaskSyncRequest](#flyteidl-admin-ExecuteTaskSyncRequest) stream | [.flyteidl.admin.ExecuteTaskSyncResponse](#flyteidl-admin-ExecuteTaskSyncResponse) stream | ExecuteTaskSync streams the create request and inputs to the agent service and streams the outputs back. |






## flyteidl/service/admin.proto










### AdminService {#flyteidl-service-AdminService}
The following defines an RPC service that is also served over HTTP via grpc-gateway.
Standard response codes for both are defined here: https://github.com/grpc-ecosystem/grpc-gateway/blob/master/runtime/errors.go

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| CreateTask | [.flyteidl.admin.TaskCreateRequest](#flyteidl-admin-TaskCreateRequest) | [.flyteidl.admin.TaskCreateResponse](#flyteidl-admin-TaskCreateResponse) | Create and upload a :ref:`ref_flyteidl.admin.Task` definition |
| GetTask | [.flyteidl.admin.ObjectGetRequest](#flyteidl-admin-ObjectGetRequest) | [.flyteidl.admin.Task](#flyteidl-admin-Task) | Fetch a :ref:`ref_flyteidl.admin.Task` definition. |
| ListTaskIds | [.flyteidl.admin.NamedEntityIdentifierListRequest](#flyteidl-admin-NamedEntityIdentifierListRequest) | [.flyteidl.admin.NamedEntityIdentifierList](#flyteidl-admin-NamedEntityIdentifierList) | Fetch a list of :ref:`ref_flyteidl.admin.NamedEntityIdentifier` of task objects. |
| ListTasks | [.flyteidl.admin.ResourceListRequest](#flyteidl-admin-ResourceListRequest) | [.flyteidl.admin.TaskList](#flyteidl-admin-TaskList) | Fetch a list of :ref:`ref_flyteidl.admin.Task` definitions. |
| CreateWorkflow | [.flyteidl.admin.WorkflowCreateRequest](#flyteidl-admin-WorkflowCreateRequest) | [.flyteidl.admin.WorkflowCreateResponse](#flyteidl-admin-WorkflowCreateResponse) | Create and upload a :ref:`ref_flyteidl.admin.Workflow` definition |
| GetWorkflow | [.flyteidl.admin.ObjectGetRequest](#flyteidl-admin-ObjectGetRequest) | [.flyteidl.admin.Workflow](#flyteidl-admin-Workflow) | Fetch a :ref:`ref_flyteidl.admin.Workflow` definition. |
| ListWorkflowIds | [.flyteidl.admin.NamedEntityIdentifierListRequest](#flyteidl-admin-NamedEntityIdentifierListRequest) | [.flyteidl.admin.NamedEntityIdentifierList](#flyteidl-admin-NamedEntityIdentifierList) | Fetch a list of :ref:`ref_flyteidl.admin.NamedEntityIdentifier` of workflow objects. |
| ListWorkflows | [.flyteidl.admin.ResourceListRequest](#flyteidl-admin-ResourceListRequest) | [.flyteidl.admin.WorkflowList](#flyteidl-admin-WorkflowList) | Fetch a list of :ref:`ref_flyteidl.admin.Workflow` definitions. |
| CreateLaunchPlan | [.flyteidl.admin.LaunchPlanCreateRequest](#flyteidl-admin-LaunchPlanCreateRequest) | [.flyteidl.admin.LaunchPlanCreateResponse](#flyteidl-admin-LaunchPlanCreateResponse) | Create and upload a :ref:`ref_flyteidl.admin.LaunchPlan` definition |
| GetLaunchPlan | [.flyteidl.admin.ObjectGetRequest](#flyteidl-admin-ObjectGetRequest) | [.flyteidl.admin.LaunchPlan](#flyteidl-admin-LaunchPlan) | Fetch a :ref:`ref_flyteidl.admin.LaunchPlan` definition. |
| GetActiveLaunchPlan | [.flyteidl.admin.ActiveLaunchPlanRequest](#flyteidl-admin-ActiveLaunchPlanRequest) | [.flyteidl.admin.LaunchPlan](#flyteidl-admin-LaunchPlan) | Fetch the active version of a :ref:`ref_flyteidl.admin.LaunchPlan`. |
| ListActiveLaunchPlans | [.flyteidl.admin.ActiveLaunchPlanListRequest](#flyteidl-admin-ActiveLaunchPlanListRequest) | [.flyteidl.admin.LaunchPlanList](#flyteidl-admin-LaunchPlanList) | List active versions of :ref:`ref_flyteidl.admin.LaunchPlan`. |
| ListLaunchPlanIds | [.flyteidl.admin.NamedEntityIdentifierListRequest](#flyteidl-admin-NamedEntityIdentifierListRequest) | [.flyteidl.admin.NamedEntityIdentifierList](#flyteidl-admin-NamedEntityIdentifierList) | Fetch a list of :ref:`ref_flyteidl.admin.NamedEntityIdentifier` of launch plan objects. |
| ListLaunchPlans | [.flyteidl.admin.ResourceListRequest](#flyteidl-admin-ResourceListRequest) | [.flyteidl.admin.LaunchPlanList](#flyteidl-admin-LaunchPlanList) | Fetch a list of :ref:`ref_flyteidl.admin.LaunchPlan` definitions. |
| UpdateLaunchPlan | [.flyteidl.admin.LaunchPlanUpdateRequest](#flyteidl-admin-LaunchPlanUpdateRequest) | [.flyteidl.admin.LaunchPlanUpdateResponse](#flyteidl-admin-LaunchPlanUpdateResponse) | Updates the status of a registered :ref:`ref_flyteidl.admin.LaunchPlan`. |
| CreateExecution | [.flyteidl.admin.ExecutionCreateRequest](#flyteidl-admin-ExecutionCreateRequest) | [.flyteidl.admin.ExecutionCreateResponse](#flyteidl-admin-ExecutionCreateResponse) | Triggers the creation of a :ref:`ref_flyteidl.admin.Execution` |
| RelaunchExecution | [.flyteidl.admin.ExecutionRelaunchRequest](#flyteidl-admin-ExecutionRelaunchRequest) | [.flyteidl.admin.ExecutionCreateResponse](#flyteidl-admin-ExecutionCreateResponse) | Triggers the creation of an identical :ref:`ref_flyteidl.admin.Execution` |
| RecoverExecution | [.flyteidl.admin.ExecutionRecoverRequest](#flyteidl-admin-ExecutionRecoverRequest) | [.flyteidl.admin.ExecutionCreateResponse](#flyteidl-admin-ExecutionCreateResponse) | Recreates a previously-run workflow execution that will only start executing from the last known failure point. In Recover mode, users cannot change any input parameters or update the version of the execution. This is extremely useful to recover from system errors and byzantine faults like - Loss of K8s cluster, bugs in platform or instability, machine failures, downstream system failures (downstream services), or simply to recover executions that failed because of retry exhaustion and should complete if tried again. See :ref:`ref_flyteidl.admin.ExecutionRecoverRequest` for more details. |
| GetExecution | [.flyteidl.admin.WorkflowExecutionGetRequest](#flyteidl-admin-WorkflowExecutionGetRequest) | [.flyteidl.admin.Execution](#flyteidl-admin-Execution) | Fetches a :ref:`ref_flyteidl.admin.Execution`. |
| UpdateExecution | [.flyteidl.admin.ExecutionUpdateRequest](#flyteidl-admin-ExecutionUpdateRequest) | [.flyteidl.admin.ExecutionUpdateResponse](#flyteidl-admin-ExecutionUpdateResponse) | Update execution belonging to project domain :ref:`ref_flyteidl.admin.Execution`. |
| GetExecutionData | [.flyteidl.admin.WorkflowExecutionGetDataRequest](#flyteidl-admin-WorkflowExecutionGetDataRequest) | [.flyteidl.admin.WorkflowExecutionGetDataResponse](#flyteidl-admin-WorkflowExecutionGetDataResponse) | Fetches input and output data for a :ref:`ref_flyteidl.admin.Execution`. |
| ListExecutions | [.flyteidl.admin.ResourceListRequest](#flyteidl-admin-ResourceListRequest) | [.flyteidl.admin.ExecutionList](#flyteidl-admin-ExecutionList) | Fetch a list of :ref:`ref_flyteidl.admin.Execution`. |
| TerminateExecution | [.flyteidl.admin.ExecutionTerminateRequest](#flyteidl-admin-ExecutionTerminateRequest) | [.flyteidl.admin.ExecutionTerminateResponse](#flyteidl-admin-ExecutionTerminateResponse) | Terminates an in-progress :ref:`ref_flyteidl.admin.Execution`. |
| GetNodeExecution | [.flyteidl.admin.NodeExecutionGetRequest](#flyteidl-admin-NodeExecutionGetRequest) | [.flyteidl.admin.NodeExecution](#flyteidl-admin-NodeExecution) | Fetches a :ref:`ref_flyteidl.admin.NodeExecution`. |
| GetDynamicNodeWorkflow | [.flyteidl.admin.GetDynamicNodeWorkflowRequest](#flyteidl-admin-GetDynamicNodeWorkflowRequest) | [.flyteidl.admin.DynamicNodeWorkflowResponse](#flyteidl-admin-DynamicNodeWorkflowResponse) | Fetches a :ref:`ref_flyteidl.admin.DynamicNodeWorkflowResponse`. |
| ListNodeExecutions | [.flyteidl.admin.NodeExecutionListRequest](#flyteidl-admin-NodeExecutionListRequest) | [.flyteidl.admin.NodeExecutionList](#flyteidl-admin-NodeExecutionList) | Fetch a list of :ref:`ref_flyteidl.admin.NodeExecution`. |
| ListNodeExecutionsForTask | [.flyteidl.admin.NodeExecutionForTaskListRequest](#flyteidl-admin-NodeExecutionForTaskListRequest) | [.flyteidl.admin.NodeExecutionList](#flyteidl-admin-NodeExecutionList) | Fetch a list of :ref:`ref_flyteidl.admin.NodeExecution` launched by the reference :ref:`ref_flyteidl.admin.TaskExecution`. |
| GetNodeExecutionData | [.flyteidl.admin.NodeExecutionGetDataRequest](#flyteidl-admin-NodeExecutionGetDataRequest) | [.flyteidl.admin.NodeExecutionGetDataResponse](#flyteidl-admin-NodeExecutionGetDataResponse) | Fetches input and output data for a :ref:`ref_flyteidl.admin.NodeExecution`. |
| RegisterProject | [.flyteidl.admin.ProjectRegisterRequest](#flyteidl-admin-ProjectRegisterRequest) | [.flyteidl.admin.ProjectRegisterResponse](#flyteidl-admin-ProjectRegisterResponse) | Registers a :ref:`ref_flyteidl.admin.Project` with the Flyte deployment. |
| UpdateProject | [.flyteidl.admin.Project](#flyteidl-admin-Project) | [.flyteidl.admin.ProjectUpdateResponse](#flyteidl-admin-ProjectUpdateResponse) | Updates an existing :ref:`ref_flyteidl.admin.Project` flyteidl.admin.Project should be passed but the domains property should be empty; it will be ignored in the handler as domains cannot be updated via this API. |
| GetProject | [.flyteidl.admin.ProjectGetRequest](#flyteidl-admin-ProjectGetRequest) | [.flyteidl.admin.Project](#flyteidl-admin-Project) | Fetches a :ref:`ref_flyteidl.admin.Project` |
| ListProjects | [.flyteidl.admin.ProjectListRequest](#flyteidl-admin-ProjectListRequest) | [.flyteidl.admin.Projects](#flyteidl-admin-Projects) | Fetches a list of :ref:`ref_flyteidl.admin.Project` |
| GetDomains | [.flyteidl.admin.GetDomainRequest](#flyteidl-admin-GetDomainRequest) | [.flyteidl.admin.GetDomainsResponse](#flyteidl-admin-GetDomainsResponse) |  |
| CreateWorkflowEvent | [.flyteidl.admin.WorkflowExecutionEventRequest](#flyteidl-admin-WorkflowExecutionEventRequest) | [.flyteidl.admin.WorkflowExecutionEventResponse](#flyteidl-admin-WorkflowExecutionEventResponse) | Indicates a :ref:`ref_flyteidl.event.WorkflowExecutionEvent` has occurred. |
| CreateNodeEvent | [.flyteidl.admin.NodeExecutionEventRequest](#flyteidl-admin-NodeExecutionEventRequest) | [.flyteidl.admin.NodeExecutionEventResponse](#flyteidl-admin-NodeExecutionEventResponse) | Indicates a :ref:`ref_flyteidl.event.NodeExecutionEvent` has occurred. |
| CreateTaskEvent | [.flyteidl.admin.TaskExecutionEventRequest](#flyteidl-admin-TaskExecutionEventRequest) | [.flyteidl.admin.TaskExecutionEventResponse](#flyteidl-admin-TaskExecutionEventResponse) | Indicates a :ref:`ref_flyteidl.event.TaskExecutionEvent` has occurred. |
| GetTaskExecution | [.flyteidl.admin.TaskExecutionGetRequest](#flyteidl-admin-TaskExecutionGetRequest) | [.flyteidl.admin.TaskExecution](#flyteidl-admin-TaskExecution) | Fetches a :ref:`ref_flyteidl.admin.TaskExecution`. |
| ListTaskExecutions | [.flyteidl.admin.TaskExecutionListRequest](#flyteidl-admin-TaskExecutionListRequest) | [.flyteidl.admin.TaskExecutionList](#flyteidl-admin-TaskExecutionList) | Fetches a list of :ref:`ref_flyteidl.admin.TaskExecution`. |
| GetTaskExecutionData | [.flyteidl.admin.TaskExecutionGetDataRequest](#flyteidl-admin-TaskExecutionGetDataRequest) | [.flyteidl.admin.TaskExecutionGetDataResponse](#flyteidl-admin-TaskExecutionGetDataResponse) | Fetches input and output data for a :ref:`ref_flyteidl.admin.TaskExecution`. |
| UpdateProjectDomainAttributes | [.flyteidl.admin.ProjectDomainAttributesUpdateRequest](#flyteidl-admin-ProjectDomainAttributesUpdateRequest) | [.flyteidl.admin.ProjectDomainAttributesUpdateResponse](#flyteidl-admin-ProjectDomainAttributesUpdateResponse) | Creates or updates custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a project and domain. |
| GetProjectDomainAttributes | [.flyteidl.admin.ProjectDomainAttributesGetRequest](#flyteidl-admin-ProjectDomainAttributesGetRequest) | [.flyteidl.admin.ProjectDomainAttributesGetResponse](#flyteidl-admin-ProjectDomainAttributesGetResponse) | Fetches custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a project and domain. |
| DeleteProjectDomainAttributes | [.flyteidl.admin.ProjectDomainAttributesDeleteRequest](#flyteidl-admin-ProjectDomainAttributesDeleteRequest) | [.flyteidl.admin.ProjectDomainAttributesDeleteResponse](#flyteidl-admin-ProjectDomainAttributesDeleteResponse) | Deletes custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a project and domain. |
| UpdateProjectAttributes | [.flyteidl.admin.ProjectAttributesUpdateRequest](#flyteidl-admin-ProjectAttributesUpdateRequest) | [.flyteidl.admin.ProjectAttributesUpdateResponse](#flyteidl-admin-ProjectAttributesUpdateResponse) | Creates or updates custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` at the project level |
| GetProjectAttributes | [.flyteidl.admin.ProjectAttributesGetRequest](#flyteidl-admin-ProjectAttributesGetRequest) | [.flyteidl.admin.ProjectAttributesGetResponse](#flyteidl-admin-ProjectAttributesGetResponse) | Fetches custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a project and domain. |
| DeleteProjectAttributes | [.flyteidl.admin.ProjectAttributesDeleteRequest](#flyteidl-admin-ProjectAttributesDeleteRequest) | [.flyteidl.admin.ProjectAttributesDeleteResponse](#flyteidl-admin-ProjectAttributesDeleteResponse) | Deletes custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a project and domain. |
| UpdateWorkflowAttributes | [.flyteidl.admin.WorkflowAttributesUpdateRequest](#flyteidl-admin-WorkflowAttributesUpdateRequest) | [.flyteidl.admin.WorkflowAttributesUpdateResponse](#flyteidl-admin-WorkflowAttributesUpdateResponse) | Creates or updates custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a project, domain and workflow. |
| GetWorkflowAttributes | [.flyteidl.admin.WorkflowAttributesGetRequest](#flyteidl-admin-WorkflowAttributesGetRequest) | [.flyteidl.admin.WorkflowAttributesGetResponse](#flyteidl-admin-WorkflowAttributesGetResponse) | Fetches custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a project, domain and workflow. |
| DeleteWorkflowAttributes | [.flyteidl.admin.WorkflowAttributesDeleteRequest](#flyteidl-admin-WorkflowAttributesDeleteRequest) | [.flyteidl.admin.WorkflowAttributesDeleteResponse](#flyteidl-admin-WorkflowAttributesDeleteResponse) | Deletes custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a project, domain and workflow. |
| ListMatchableAttributes | [.flyteidl.admin.ListMatchableAttributesRequest](#flyteidl-admin-ListMatchableAttributesRequest) | [.flyteidl.admin.ListMatchableAttributesResponse](#flyteidl-admin-ListMatchableAttributesResponse) | Lists custom :ref:`ref_flyteidl.admin.MatchableAttributesConfiguration` for a specific resource type. |
| ListNamedEntities | [.flyteidl.admin.NamedEntityListRequest](#flyteidl-admin-NamedEntityListRequest) | [.flyteidl.admin.NamedEntityList](#flyteidl-admin-NamedEntityList) | Returns a list of :ref:`ref_flyteidl.admin.NamedEntity` objects. |
| GetNamedEntity | [.flyteidl.admin.NamedEntityGetRequest](#flyteidl-admin-NamedEntityGetRequest) | [.flyteidl.admin.NamedEntity](#flyteidl-admin-NamedEntity) | Returns a :ref:`ref_flyteidl.admin.NamedEntity` object. |
| UpdateNamedEntity | [.flyteidl.admin.NamedEntityUpdateRequest](#flyteidl-admin-NamedEntityUpdateRequest) | [.flyteidl.admin.NamedEntityUpdateResponse](#flyteidl-admin-NamedEntityUpdateResponse) | Updates a :ref:`ref_flyteidl.admin.NamedEntity` object. |
| GetVersion | [.flyteidl.admin.GetVersionRequest](#flyteidl-admin-GetVersionRequest) | [.flyteidl.admin.GetVersionResponse](#flyteidl-admin-GetVersionResponse) |  |
| GetDescriptionEntity | [.flyteidl.admin.ObjectGetRequest](#flyteidl-admin-ObjectGetRequest) | [.flyteidl.admin.DescriptionEntity](#flyteidl-admin-DescriptionEntity) | Fetch a :ref:`ref_flyteidl.admin.DescriptionEntity` object. |
| ListDescriptionEntities | [.flyteidl.admin.DescriptionEntityListRequest](#flyteidl-admin-DescriptionEntityListRequest) | [.flyteidl.admin.DescriptionEntityList](#flyteidl-admin-DescriptionEntityList) | Fetch a list of :ref:`ref_flyteidl.admin.DescriptionEntity` definitions. |
| GetExecutionMetrics | [.flyteidl.admin.WorkflowExecutionGetMetricsRequest](#flyteidl-admin-WorkflowExecutionGetMetricsRequest) | [.flyteidl.admin.WorkflowExecutionGetMetricsResponse](#flyteidl-admin-WorkflowExecutionGetMetricsResponse) | Fetches runtime metrics for a :ref:`ref_flyteidl.admin.Execution`. |






## flyteidl/event/cloudevents.proto




### CloudEventExecutionStart {#flyteidl-event-CloudEventExecutionStart}
This event is to be sent by Admin after it creates an execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| execution_id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | The execution created. |
| launch_plan_id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | The launch plan used. |
| workflow_id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  |  |
| artifact_ids | [flyteidl.core.ArtifactID](#flyteidl-core-ArtifactID) | repeated | Artifact inputs to the workflow execution for which we have the full Artifact ID. These are likely the result of artifact queries that are run. |
| artifact_trackers | string | repeated | Artifact inputs to the workflow execution for which we only have the tracking bit that's installed into the Literal's metadata by the Artifact service. |
| principal | string |  |  |







### CloudEventNodeExecution {#flyteidl-event-CloudEventNodeExecution}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| raw_event | [NodeExecutionEvent](#flyteidl-event-NodeExecutionEvent) |  |  |
| task_exec_id | [flyteidl.core.TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  | The relevant task execution if applicable |
| output_interface | [flyteidl.core.TypedInterface](#flyteidl-core-TypedInterface) |  | The typed interface for the task that produced the event. |
| artifact_ids | [flyteidl.core.ArtifactID](#flyteidl-core-ArtifactID) | repeated | The following are ExecutionMetadata fields We can't have the ExecutionMetadata object directly because of import cycle |
| principal | string |  |  |
| launch_plan_id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | The ID of the LP that generated the execution that generated the Artifact. Here for provenance information. Launch plan IDs are easier to get than workflow IDs so we'll use these for now. |
| labels | [CloudEventNodeExecution.LabelsEntry](#flyteidl-event-CloudEventNodeExecution-LabelsEntry) | repeated | We can't have the ExecutionMetadata object directly because of import cycle |







### CloudEventNodeExecution.LabelsEntry {#flyteidl-event-CloudEventNodeExecution-LabelsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### CloudEventTaskExecution {#flyteidl-event-CloudEventTaskExecution}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| raw_event | [TaskExecutionEvent](#flyteidl-event-TaskExecutionEvent) |  |  |
| labels | [CloudEventTaskExecution.LabelsEntry](#flyteidl-event-CloudEventTaskExecution-LabelsEntry) | repeated | We can't have the ExecutionMetadata object directly because of import cycle |







### CloudEventTaskExecution.LabelsEntry {#flyteidl-event-CloudEventTaskExecution-LabelsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### CloudEventWorkflowExecution {#flyteidl-event-CloudEventWorkflowExecution}
This is the cloud event parallel to the raw WorkflowExecutionEvent message. It's filled in with additional
information that downstream consumers may find useful.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| raw_event | [WorkflowExecutionEvent](#flyteidl-event-WorkflowExecutionEvent) |  |  |
| output_interface | [flyteidl.core.TypedInterface](#flyteidl-core-TypedInterface) |  |  |
| artifact_ids | [flyteidl.core.ArtifactID](#flyteidl-core-ArtifactID) | repeated | The following are ExecutionMetadata fields We can't have the ExecutionMetadata object directly because of import cycle |
| reference_execution | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  |  |
| principal | string |  |  |
| launch_plan_id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | The ID of the LP that generated the execution that generated the Artifact. Here for provenance information. Launch plan IDs are easier to get than workflow IDs so we'll use these for now. |
| labels | [CloudEventWorkflowExecution.LabelsEntry](#flyteidl-event-CloudEventWorkflowExecution-LabelsEntry) | repeated | We can't have the ExecutionMetadata object directly because of import cycle |







### CloudEventWorkflowExecution.LabelsEntry {#flyteidl-event-CloudEventWorkflowExecution-LabelsEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |
















## flyteidl/event/event.proto




### DynamicWorkflowNodeMetadata {#flyteidl-event-DynamicWorkflowNodeMetadata}
For dynamic workflow nodes we send information about the dynamic workflow definition that gets generated.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | id represents the unique identifier of the workflow. |
| compiled_workflow | [flyteidl.core.CompiledWorkflowClosure](#flyteidl-core-CompiledWorkflowClosure) |  | Represents the compiled representation of the embedded dynamic workflow. |
| dynamic_job_spec_uri | string |  | dynamic_job_spec_uri is the location of the DynamicJobSpec proto message for this DynamicWorkflow. This is required to correctly recover partially completed executions where the workflow has already been compiled. |







### EventReason {#flyteidl-event-EventReason}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reason | string |  | An explanation for this event |
| occurred_at | google.protobuf.Timestamp |  | The time this reason occurred |







### ExternalResourceInfo {#flyteidl-event-ExternalResourceInfo}
This message contains metadata about external resources produced or used by a specific task execution.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| external_id | string |  | Identifier for an external resource created by this task execution, for example Qubole query ID or presto query ids. |
| index | uint32 |  | A unique index for the external resource with respect to all external resources for this task. Although the identifier may change between task reporting events or retries, this will remain the same to enable aggregating information from multiple reports. |
| retry_attempt | uint32 |  | Retry attempt number for this external resource, ie., 2 for the second attempt |
| phase | [flyteidl.core.TaskExecution.Phase](#flyteidl-core-TaskExecution-Phase) |  | Phase associated with the external resource |
| cache_status | [flyteidl.core.CatalogCacheStatus](#flyteidl-core-CatalogCacheStatus) |  | Captures the status of caching for this external resource execution. |
| logs | [flyteidl.core.TaskLog](#flyteidl-core-TaskLog) | repeated | log information for the external resource execution |
| workflow_node_metadata | [WorkflowNodeMetadata](#flyteidl-event-WorkflowNodeMetadata) |  |  |
| custom_info | google.protobuf.Struct |  | Extensible field for custom, plugin-specific info |







### NodeExecutionEvent {#flyteidl-event-NodeExecutionEvent}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | Unique identifier for this node execution |
| producer_id | string |  | the id of the originator (Propeller) of the event |
| phase | [flyteidl.core.NodeExecution.Phase](#flyteidl-core-NodeExecution-Phase) |  |  |
| occurred_at | google.protobuf.Timestamp |  | This timestamp represents when the original event occurred, it is generated by the executor of the node. |
| input_uri | string |  |  |
| input_data | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Raw input data consumed by this node execution. |
| output_uri | string |  | URL to the output of the execution, it encodes all the information including Cloud source provider. ie., s3://... |
| error | [flyteidl.core.ExecutionError](#flyteidl-core-ExecutionError) |  | Error information for the execution |
| output_data | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Raw output data produced by this node execution. |
| workflow_node_metadata | [WorkflowNodeMetadata](#flyteidl-event-WorkflowNodeMetadata) |  |  |
| task_node_metadata | [TaskNodeMetadata](#flyteidl-event-TaskNodeMetadata) |  |  |
| parent_task_metadata | [ParentTaskExecutionMetadata](#flyteidl-event-ParentTaskExecutionMetadata) |  | [To be deprecated] Specifies which task (if any) launched this node. |
| parent_node_metadata | [ParentNodeExecutionMetadata](#flyteidl-event-ParentNodeExecutionMetadata) |  | Specifies the parent node of the current node execution. Node executions at level zero will not have a parent node. |
| retry_group | string |  | Retry group to indicate grouping of nodes by retries |
| spec_node_id | string |  | Identifier of the node in the original workflow/graph This maps to value of WorkflowTemplate.nodes[X].id |
| node_name | string |  | Friendly readable name for the node |
| event_version | int32 |  |  |
| is_parent | bool |  | Whether this node launched a subworkflow. |
| is_dynamic | bool |  | Whether this node yielded a dynamic workflow. |
| deck_uri | string |  | String location uniquely identifying where the deck HTML file is NativeUrl specifies the url in the format of the configured storage provider (e.g. s3://my-bucket/randomstring/suffix.tar) |
| reported_at | google.protobuf.Timestamp |  | This timestamp represents the instant when the event was reported by the executing framework. For example, when first processing a node the `occurred_at` timestamp should be the instant propeller makes progress, so when literal inputs are initially copied. The event however will not be sent until after the copy completes. Extracting both of these timestamps facilitates a more accurate portrayal of the evaluation time-series. |
| is_array | bool |  | Indicates if this node is an ArrayNode. |
| target_entity | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | So that Admin doesn't have to rebuild the node execution graph to find the target entity, propeller will fill this in optionally - currently this is only filled in for subworkflows. This is the ID of the subworkflow corresponding to this node execution. It is difficult to find because Admin only sees one node at a time. A subworkflow could be nested multiple layers deep, and you'd need to access the correct workflow template to know the target subworkflow. |
| is_in_dynamic_chain | bool |  | Tasks and subworkflows (but not launch plans) that are run within a dynamic task are effectively independent of the tasks that are registered in Admin's db. Confusingly, they are often identical, but sometimes they are not even registered at all. Similar to the target_entity field, at the time Admin receives this event, it has no idea if the relevant execution entity is was registered, or dynamic. This field indicates that the target_entity ID, as well as task IDs in any corresponding Task Executions, should not be used to looked up the task in Admin's db. |
| is_eager | bool |  | Whether this node launched an eager task. |







### ParentNodeExecutionMetadata {#flyteidl-event-ParentNodeExecutionMetadata}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_id | string |  | Unique identifier of the parent node id within the execution This is value of core.NodeExecutionIdentifier.node_id of the parent node |







### ParentTaskExecutionMetadata {#flyteidl-event-ParentTaskExecutionMetadata}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [flyteidl.core.TaskExecutionIdentifier](#flyteidl-core-TaskExecutionIdentifier) |  |  |







### ResourcePoolInfo {#flyteidl-event-ResourcePoolInfo}
This message holds task execution metadata specific to resource allocation used to manage concurrent
executions for a project namespace.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| allocation_token | string |  | Unique resource ID used to identify this execution when allocating a token. |
| namespace | string |  | Namespace under which this task execution requested an allocation token. |







### TaskExecutionEvent {#flyteidl-event-TaskExecutionEvent}
Plugin specific execution event information. For tasks like Python, Hive, Spark, DynamicJob.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [flyteidl.core.Identifier](#flyteidl-core-Identifier) |  | ID of the task. In combination with the retryAttempt this will indicate the task execution uniquely for a given parent node execution. |
| parent_node_execution_id | [flyteidl.core.NodeExecutionIdentifier](#flyteidl-core-NodeExecutionIdentifier) |  | A task execution is always kicked off by a node execution, the event consumer will use the parent_id to relate the task to it's parent node execution |
| retry_attempt | uint32 |  | retry attempt number for this task, ie., 2 for the second attempt |
| phase | [flyteidl.core.TaskExecution.Phase](#flyteidl-core-TaskExecution-Phase) |  | Phase associated with the event |
| producer_id | string |  | id of the process that sent this event, mainly for trace debugging |
| logs | [flyteidl.core.TaskLog](#flyteidl-core-TaskLog) | repeated | log information for the task execution |
| occurred_at | google.protobuf.Timestamp |  | This timestamp represents when the original event occurred, it is generated by the executor of the task. |
| input_uri | string |  | URI of the input file, it encodes all the information including Cloud source provider. ie., s3://... |
| input_data | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Raw input data consumed by this task execution. |
| output_uri | string |  | URI to the output of the execution, it will be in a format that encodes all the information including Cloud source provider. ie., s3://... |
| error | [flyteidl.core.ExecutionError](#flyteidl-core-ExecutionError) |  | Error information for the execution |
| output_data | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Raw output data produced by this task execution. |
| custom_info | google.protobuf.Struct |  | Custom data that the task plugin sends back. This is extensible to allow various plugins in the system. |
| phase_version | uint32 |  | Some phases, like RUNNING, can send multiple events with changed metadata (new logs, additional custom_info, etc) that should be recorded regardless of the lack of phase change. The version field should be incremented when metadata changes across the duration of an individual phase. |
| reason | string |  | **Deprecated.** An optional explanation for the phase transition. Deprecated: Use reasons instead. |
| reasons | [EventReason](#flyteidl-event-EventReason) | repeated | An optional list of explanations for the phase transition. |
| task_type | string |  | A predefined yet extensible Task type identifier. If the task definition is already registered in flyte admin this type will be identical, but not all task executions necessarily use pre-registered definitions and this type is useful to render the task in the UI, filter task executions, etc. |
| metadata | [TaskExecutionMetadata](#flyteidl-event-TaskExecutionMetadata) |  | Metadata around how a task was executed. |
| event_version | int32 |  | The event version is used to indicate versioned changes in how data is reported using this proto message. For example, event_verison >gt; 0 means that maps tasks report logs using the TaskExecutionMetadata ExternalResourceInfo fields for each subtask rather than the TaskLog in this message. |
| reported_at | google.protobuf.Timestamp |  | This timestamp represents the instant when the event was reported by the executing framework. For example, a k8s pod task may be marked completed at (ie. `occurred_at`) the instant the container running user code completes, but this event will not be reported until the pod is marked as completed. Extracting both of these timestamps facilitates a more accurate portrayal of the evaluation time-series. |







### TaskExecutionMetadata {#flyteidl-event-TaskExecutionMetadata}
Holds metadata around how a task was executed.
As a task transitions across event phases during execution some attributes, such its generated name, generated external resources,
and more may grow in size but not change necessarily based on the phase transition that sparked the event update.
Metadata is a container for these attributes across the task execution lifecycle.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| generated_name | string |  | Unique, generated name for this task execution used by the backend. |
| external_resources | [ExternalResourceInfo](#flyteidl-event-ExternalResourceInfo) | repeated | Additional data on external resources on other back-ends or platforms (e.g. Hive, Qubole, etc) launched by this task execution. |
| resource_pool_info | [ResourcePoolInfo](#flyteidl-event-ResourcePoolInfo) | repeated | Includes additional data on concurrent resource management used during execution.. This is a repeated field because a plugin can request multiple resource allocations during execution. |
| plugin_identifier | string |  | The identifier of the plugin used to execute this task. |
| instance_class | [TaskExecutionMetadata.InstanceClass](#flyteidl-event-TaskExecutionMetadata-InstanceClass) |  |  |







### TaskNodeMetadata {#flyteidl-event-TaskNodeMetadata}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cache_status | [flyteidl.core.CatalogCacheStatus](#flyteidl-core-CatalogCacheStatus) |  | Captures the status of caching for this execution. |
| catalog_key | [flyteidl.core.CatalogMetadata](#flyteidl-core-CatalogMetadata) |  | This structure carries the catalog artifact information |
| reservation_status | [flyteidl.core.CatalogReservation.Status](#flyteidl-core-CatalogReservation-Status) |  | Captures the status of cache reservations for this execution. |
| checkpoint_uri | string |  | The latest checkpoint location |
| dynamic_workflow | [DynamicWorkflowNodeMetadata](#flyteidl-event-DynamicWorkflowNodeMetadata) |  | In the case this task launched a dynamic workflow we capture its structure here. |







### WorkflowExecutionEvent {#flyteidl-event-WorkflowExecutionEvent}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| execution_id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  | Workflow execution id |
| producer_id | string |  | the id of the originator (Propeller) of the event |
| phase | [flyteidl.core.WorkflowExecution.Phase](#flyteidl-core-WorkflowExecution-Phase) |  |  |
| occurred_at | google.protobuf.Timestamp |  | This timestamp represents when the original event occurred, it is generated by the executor of the workflow. |
| output_uri | string |  | URL to the output of the execution, it encodes all the information including Cloud source provider. ie., s3://... |
| error | [flyteidl.core.ExecutionError](#flyteidl-core-ExecutionError) |  | Error information for the execution |
| output_data | [flyteidl.core.LiteralMap](#flyteidl-core-LiteralMap) |  | Raw output data produced by this workflow execution. |







### WorkflowNodeMetadata {#flyteidl-event-WorkflowNodeMetadata}
For Workflow Nodes we need to send information about the workflow that's launched



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| execution_id | [flyteidl.core.WorkflowExecutionIdentifier](#flyteidl-core-WorkflowExecutionIdentifier) |  |  |









### TaskExecutionMetadata.InstanceClass {#flyteidl-event-TaskExecutionMetadata-InstanceClass}
Includes the broad category of machine used for this specific task execution.

| Name | Number | Description |
| ---- | ------ | ----------- |
| DEFAULT | 0 | The default instance class configured for the flyte application platform. |
| INTERRUPTIBLE | 1 | The instance class configured for interruptible tasks. |











## flyteidl/datacatalog/datacatalog.proto




### AddTagRequest {#datacatalog-AddTagRequest}
Request message for tagging an Artifact.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tag | [Tag](#datacatalog-Tag) |  |  |







### AddTagResponse {#datacatalog-AddTagResponse}
Response message for tagging an Artifact.







### Artifact {#datacatalog-Artifact}
Artifact message. It is composed of several string fields.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | string |  | The unique ID of the artifact |
| dataset | [DatasetID](#datacatalog-DatasetID) |  | The Dataset that the artifact belongs to |
| data | [ArtifactData](#datacatalog-ArtifactData) | repeated | A list of data that is associated with the artifact |
| metadata | [Metadata](#datacatalog-Metadata) |  | Free-form metadata associated with the artifact |
| partitions | [Partition](#datacatalog-Partition) | repeated |  |
| tags | [Tag](#datacatalog-Tag) | repeated |  |
| created_at | google.protobuf.Timestamp |  | creation timestamp of artifact, autogenerated by service |







### ArtifactData {#datacatalog-ArtifactData}
ArtifactData that belongs to an artifact



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  |  |
| value | flyteidl.core.Literal |  |  |







### ArtifactPropertyFilter {#datacatalog-ArtifactPropertyFilter}
Artifact properties we can filter by



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact_id | string |  |  |







### CreateArtifactRequest {#datacatalog-CreateArtifactRequest}
Request message for creating an Artifact and its associated artifact Data.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact | [Artifact](#datacatalog-Artifact) |  |  |







### CreateArtifactResponse {#datacatalog-CreateArtifactResponse}
Response message for creating an Artifact.







### CreateDatasetRequest {#datacatalog-CreateDatasetRequest}
Request message for creating a Dataset.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dataset | [Dataset](#datacatalog-Dataset) |  |  |







### CreateDatasetResponse {#datacatalog-CreateDatasetResponse}
Response message for creating a Dataset







### Dataset {#datacatalog-Dataset}
Dataset message. It is uniquely identified by DatasetID.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [DatasetID](#datacatalog-DatasetID) |  |  |
| metadata | [Metadata](#datacatalog-Metadata) |  |  |
| partitionKeys | string | repeated |  |







### DatasetID {#datacatalog-DatasetID}
DatasetID message that is composed of several string fields.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  | The name of the project |
| name | string |  | The name of the dataset |
| domain | string |  | The domain (eg. environment) |
| version | string |  | Version of the data schema |
| UUID | string |  | UUID for the dataset (if set the above fields are optional) |
| org | string |  | Optional, org key applied to the resource. |







### DatasetPropertyFilter {#datacatalog-DatasetPropertyFilter}
Dataset properties we can filter by



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| project | string |  |  |
| name | string |  |  |
| domain | string |  |  |
| version | string |  |  |
| org | string |  | Optional, org key applied to the dataset. |







### FilterExpression {#datacatalog-FilterExpression}
Filter expression that is composed of a combination of single filters



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filters | [SinglePropertyFilter](#datacatalog-SinglePropertyFilter) | repeated |  |







### GetArtifactRequest {#datacatalog-GetArtifactRequest}
Request message for retrieving an Artifact. Retrieve an artifact based on a query handle that
can be one of artifact_id or tag. The result returned will include the artifact data and metadata
associated with the artifact.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dataset | [DatasetID](#datacatalog-DatasetID) |  |  |
| artifact_id | string |  |  |
| tag_name | string |  |  |







### GetArtifactResponse {#datacatalog-GetArtifactResponse}
Response message for retrieving an Artifact. The result returned will include the artifact data
and metadata associated with the artifact.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact | [Artifact](#datacatalog-Artifact) |  |  |







### GetDatasetRequest {#datacatalog-GetDatasetRequest}
Request message for retrieving a Dataset. The Dataset is retrieved by it's unique identifier
which is a combination of several fields.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dataset | [DatasetID](#datacatalog-DatasetID) |  |  |







### GetDatasetResponse {#datacatalog-GetDatasetResponse}
Response message for retrieving a Dataset. The response will include the metadata for the
Dataset.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dataset | [Dataset](#datacatalog-Dataset) |  |  |







### GetOrExtendReservationRequest {#datacatalog-GetOrExtendReservationRequest}
Try to acquire or extend an artifact reservation. If an active reservation exists, retrieve that instance.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reservation_id | [ReservationID](#datacatalog-ReservationID) |  | The unique ID for the reservation |
| owner_id | string |  | The unique ID of the owner for the reservation |
| heartbeat_interval | google.protobuf.Duration |  | Requested reservation extension heartbeat interval |







### GetOrExtendReservationResponse {#datacatalog-GetOrExtendReservationResponse}
Response including either a newly minted reservation or the existing reservation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reservation | [Reservation](#datacatalog-Reservation) |  | The reservation to be acquired or extended |







### KeyValuePair {#datacatalog-KeyValuePair}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### ListArtifactsRequest {#datacatalog-ListArtifactsRequest}
List the artifacts that belong to the Dataset, optionally filtered using filtered expression.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dataset | [DatasetID](#datacatalog-DatasetID) |  | Use a datasetID for which you want to retrieve the artifacts |
| filter | [FilterExpression](#datacatalog-FilterExpression) |  | Apply the filter expression to this query |
| pagination | [PaginationOptions](#datacatalog-PaginationOptions) |  | Pagination options to get a page of artifacts |







### ListArtifactsResponse {#datacatalog-ListArtifactsResponse}
Response to list artifacts



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifacts | [Artifact](#datacatalog-Artifact) | repeated | The list of artifacts |
| next_token | string |  | Token to use to request the next page, pass this into the next requests PaginationOptions |







### ListDatasetsRequest {#datacatalog-ListDatasetsRequest}
List the datasets for the given query



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [FilterExpression](#datacatalog-FilterExpression) |  | Apply the filter expression to this query |
| pagination | [PaginationOptions](#datacatalog-PaginationOptions) |  | Pagination options to get a page of datasets |







### ListDatasetsResponse {#datacatalog-ListDatasetsResponse}
List the datasets response with token for next pagination



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| datasets | [Dataset](#datacatalog-Dataset) | repeated | The list of datasets |
| next_token | string |  | Token to use to request the next page, pass this into the next requests PaginationOptions |







### Metadata {#datacatalog-Metadata}
Metadata representation for artifacts and datasets



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key_map | [Metadata.KeyMapEntry](#datacatalog-Metadata-KeyMapEntry) | repeated | key map is a dictionary of key/val strings that represent metadata |







### Metadata.KeyMapEntry {#datacatalog-Metadata-KeyMapEntry}




| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### PaginationOptions {#datacatalog-PaginationOptions}
Pagination options for making list requests



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| limit | uint32 |  | the max number of results to return |
| token | string |  | the token to pass to fetch the next page |
| sortKey | [PaginationOptions.SortKey](#datacatalog-PaginationOptions-SortKey) |  | the property that we want to sort the results by |
| sortOrder | [PaginationOptions.SortOrder](#datacatalog-PaginationOptions-SortOrder) |  | the sort order of the results |







### Partition {#datacatalog-Partition}
An artifact could have multiple partitions and each partition can have an arbitrary string key/value pair



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | string |  |  |
| value | string |  |  |







### PartitionPropertyFilter {#datacatalog-PartitionPropertyFilter}
Partition properties we can filter by



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key_val | [KeyValuePair](#datacatalog-KeyValuePair) |  |  |







### ReleaseReservationRequest {#datacatalog-ReleaseReservationRequest}
Request to release reservation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reservation_id | [ReservationID](#datacatalog-ReservationID) |  | The unique ID for the reservation |
| owner_id | string |  | The unique ID of the owner for the reservation |







### ReleaseReservationResponse {#datacatalog-ReleaseReservationResponse}
Response to release reservation







### Reservation {#datacatalog-Reservation}
A reservation including owner, heartbeat interval, expiration timestamp, and various metadata.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reservation_id | [ReservationID](#datacatalog-ReservationID) |  | The unique ID for the reservation |
| owner_id | string |  | The unique ID of the owner for the reservation |
| heartbeat_interval | google.protobuf.Duration |  | Recommended heartbeat interval to extend reservation |
| expires_at | google.protobuf.Timestamp |  | Expiration timestamp of this reservation |
| metadata | [Metadata](#datacatalog-Metadata) |  | Free-form metadata associated with the artifact |







### ReservationID {#datacatalog-ReservationID}
ReservationID message that is composed of several string fields.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dataset_id | [DatasetID](#datacatalog-DatasetID) |  | The unique ID for the reserved dataset |
| tag_name | string |  | The specific artifact tag for the reservation |







### SinglePropertyFilter {#datacatalog-SinglePropertyFilter}
A single property to filter on.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tag_filter | [TagPropertyFilter](#datacatalog-TagPropertyFilter) |  |  |
| partition_filter | [PartitionPropertyFilter](#datacatalog-PartitionPropertyFilter) |  |  |
| artifact_filter | [ArtifactPropertyFilter](#datacatalog-ArtifactPropertyFilter) |  |  |
| dataset_filter | [DatasetPropertyFilter](#datacatalog-DatasetPropertyFilter) |  |  |
| operator | [SinglePropertyFilter.ComparisonOperator](#datacatalog-SinglePropertyFilter-ComparisonOperator) |  | field 10 in case we add more entities to query |







### Tag {#datacatalog-Tag}
Tag message that is unique to a Dataset. It is associated to a single artifact and
can be retrieved by name later.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  | Name of tag |
| artifact_id | string |  | The tagged artifact |
| dataset | [DatasetID](#datacatalog-DatasetID) |  | The Dataset that this tag belongs to |







### TagPropertyFilter {#datacatalog-TagPropertyFilter}
Tag properties we can filter by



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tag_name | string |  |  |







### UpdateArtifactRequest {#datacatalog-UpdateArtifactRequest}
Request message for updating an Artifact and overwriting its associated ArtifactData.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dataset | [DatasetID](#datacatalog-DatasetID) |  | ID of dataset the artifact is associated with |
| artifact_id | string |  |  |
| tag_name | string |  |  |
| data | [ArtifactData](#datacatalog-ArtifactData) | repeated | List of data to overwrite stored artifact data with. Must contain ALL data for updated Artifact as any missing ArtifactData entries will be removed from the underlying blob storage and database. |
| metadata | [Metadata](#datacatalog-Metadata) |  | Update execution metadata(including execution domain, name, node, project data) when overwriting cache |







### UpdateArtifactResponse {#datacatalog-UpdateArtifactResponse}
Response message for updating an Artifact.



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| artifact_id | string |  | The unique ID of the artifact updated |









### PaginationOptions.SortKey {#datacatalog-PaginationOptions-SortKey}


| Name | Number | Description |
| ---- | ------ | ----------- |
| CREATION_TIME | 0 |  |




### PaginationOptions.SortOrder {#datacatalog-PaginationOptions-SortOrder}


| Name | Number | Description |
| ---- | ------ | ----------- |
| DESCENDING | 0 |  |
| ASCENDING | 1 |  |




### SinglePropertyFilter.ComparisonOperator {#datacatalog-SinglePropertyFilter-ComparisonOperator}
as use-cases come up we can add more operators, ex: gte, like, not eq etc.

| Name | Number | Description |
| ---- | ------ | ----------- |
| EQUALS | 0 |  |








### DataCatalog {#datacatalog-DataCatalog}
Data Catalog service definition
Data Catalog is a service for indexing parameterized, strongly-typed data artifacts across revisions.
Artifacts are associated with a Dataset, and can be tagged for retrieval.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| CreateDataset | [CreateDatasetRequest](#datacatalog-CreateDatasetRequest) | [CreateDatasetResponse](#datacatalog-CreateDatasetResponse) | Create a new Dataset. Datasets are unique based on the DatasetID. Datasets are logical groupings of artifacts. Each dataset can have one or more artifacts |
| GetDataset | [GetDatasetRequest](#datacatalog-GetDatasetRequest) | [GetDatasetResponse](#datacatalog-GetDatasetResponse) | Get a Dataset by the DatasetID. This returns the Dataset with the associated metadata. |
| CreateArtifact | [CreateArtifactRequest](#datacatalog-CreateArtifactRequest) | [CreateArtifactResponse](#datacatalog-CreateArtifactResponse) | Create an artifact and the artifact data associated with it. An artifact can be a hive partition or arbitrary files or data values |
| GetArtifact | [GetArtifactRequest](#datacatalog-GetArtifactRequest) | [GetArtifactResponse](#datacatalog-GetArtifactResponse) | Retrieve an artifact by an identifying handle. This returns an artifact along with the artifact data. |
| AddTag | [AddTagRequest](#datacatalog-AddTagRequest) | [AddTagResponse](#datacatalog-AddTagResponse) | Associate a tag with an artifact. Tags are unique within a Dataset. |
| ListArtifacts | [ListArtifactsRequest](#datacatalog-ListArtifactsRequest) | [ListArtifactsResponse](#datacatalog-ListArtifactsResponse) | Return a paginated list of artifacts |
| ListDatasets | [ListDatasetsRequest](#datacatalog-ListDatasetsRequest) | [ListDatasetsResponse](#datacatalog-ListDatasetsResponse) | Return a paginated list of datasets |
| UpdateArtifact | [UpdateArtifactRequest](#datacatalog-UpdateArtifactRequest) | [UpdateArtifactResponse](#datacatalog-UpdateArtifactResponse) | Updates an existing artifact, overwriting the stored artifact data in the underlying blob storage. |
| GetOrExtendReservation | [GetOrExtendReservationRequest](#datacatalog-GetOrExtendReservationRequest) | [GetOrExtendReservationResponse](#datacatalog-GetOrExtendReservationResponse) | Attempts to get or extend a reservation for the corresponding artifact. If one already exists (ie. another entity owns the reservation) then that reservation is retrieved. Once you acquire a reservation, you need to periodically extend the reservation with an identical call. If the reservation is not extended before the defined expiration, it may be acquired by another task. Note: We may have multiple concurrent tasks with the same signature and the same input that try to populate the same artifact at the same time. Thus with reservation, only one task can run at a time, until the reservation expires. Note: If task A does not extend the reservation in time and the reservation expires, another task B may take over the reservation, resulting in two tasks A and B running in parallel. So a third task C may get the Artifact from A or B, whichever writes last. |
| ReleaseReservation | [ReleaseReservationRequest](#datacatalog-ReleaseReservationRequest) | [ReleaseReservationResponse](#datacatalog-ReleaseReservationResponse) | Release the reservation when the task holding the spot fails so that the other tasks can grab the spot. |





## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| double |  | double | double | float | float64 | double | float | Float |
| float |  | float | float | float | float32 | float | float | Float |
| int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |
