window.addEventListener('DOMContentLoaded', () => {
  var url = new URL(window.location)
  if (url.searchParams.get('404') !== null) {
    const fourOFourMessage = document.querySelector('.four-notice')
    fourOFourMessage.style.display = 'block'

    const sourceUrl = new URL(url.searchParams.get('404'))
    if (['http:', 'https:'].includes(sourceUrl.protocol)) {
      const fourPageLink = document.createElement('a')
      fourPageLink.href = url.searchParams.get('404')
      fourPageLink.innerText = url.searchParams.get('404')

      const fourPage = document.querySelector('.four-page')
      fourPage.appendChild(fourPageLink)
    }
  }
})
