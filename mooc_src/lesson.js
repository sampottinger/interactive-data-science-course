/**
 * Logic to run the lesson page.
 *
 * @license BSD-3-Clause
 */

/**
 * Add click listeners for enable and disable embed.
 *
 * Add click listeners which enable and disable the video embed when
 * clicked, preventing default link events in the process. These apply to
 * all elements with the enable-video-embed-link class to enable embed and
 * all elements with the disable-video-embed-link to disable embed.
 */
function addEmbedListeners() {
  document.querySelectorAll('.enable-video-embed-link').forEach((link) => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      onEnableEmbed();
    });
  });

  document.querySelectorAll('.disable-video-embed-link').forEach((link) => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      onDisableEmbed();
    });
  });
}

/**
 * Read the preference from the cookie for embeds.
 *
 * Read the preference from the site cookie for if video embeds are
 * enabled, returning false if a preference is not yet specified.
 *
 * @return {boolean} True if video embeds are enabled and false otherwise.
 */
function getEmbedPreference() {
  return document.cookie.includes('video_embeds_enabled=true');
}

/**
 * Callback for when the user has requested video embeds be enabled.
 *
 * Callback for when the user has requested video embeds be enabled,
 * saving their preference in the site cookie and showing the embed on the
 * current page. This will overwrite any prior preferences saved.
 */
function onEnableEmbed() {
  document.cookie = 'video_embeds_enabled=true;path=/';
  showEmbed();
}

/**
 * Callback for when the user has requested video embeds be disabled.
 *
 * Callback for when the user has requested video embeds be disabled,
 * saving their preference in the site cookie and hiding the embed on the
 * current page. This will overwrite any prior preferences saved.
 */
function onDisableEmbed() {
  document.cookie = 'video_embeds_enabled=false;path=/';
  hideEmbed();
}

/**
 * Show the video embed on this page.
 *
 * Take the iframe template from video-embed-template and putting the
 * contents into video-embed-target before setting video-embed to be
 * visible.
 */
function showEmbed() {
  const template = document.getElementById('video-embed-template').innerHTML;
  document.getElementById('video-embed-target').innerHTML = template;
  document.getElementById('video-confirm').style.display = 'none';
  document.getElementById('video-embed').style.display = 'block';
}

/**
 * Hide the video embed on this page by hiding video-embed.
 */
function hideEmbed() {
  document.getElementById('video-embed-target').innerHTML = '';
  document.getElementById('video-confirm').style.display = 'block';
  document.getElementById('video-embed').style.display = 'none';
}

/**
 * Check cookie settings and initialize video embed on the page.
 *
 * Check cookie settings and initialize video embed on the page if the
 * cookie indicates that user's preference is to have embeds enabled. No
 * action taken if the cookie indicates that the user's preference is that
 * video embeds are disabled.
 */
function initEmbedGivenSettings() {
  if (getEmbedPreference()) {
    showEmbed();
  } else {
    hideEmbed();
  }
}

/**
 * Main entrypoint into lesson page logic.
 */
function main() {
  initEmbedGivenSettings();
  addEmbedListeners();
}

main();
