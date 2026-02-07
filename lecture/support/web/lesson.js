/**
 * Logic to run the lesson page.
 *
 * @license BSD-3-Clause
 */

/**
 * Add click listeners for enable and disable embed.
 *
 * Add click listeners to enable and disable the video embed (user
 * click). Callbacks will modify the user preference cookie.
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
 * Render the video embed template on this page, allowing the Vimeo integration
 * to proceed.
 */
function showEmbed() {
  const template = document.getElementById('video-embed-template').innerHTML;
  document.getElementById('video-embed-target').innerHTML = template;
  document.getElementById('video-confirm').style.display = 'none';
  document.getElementById('video-embed').style.display = 'block';
}

/**
 * Hide the video embed on this page by hiding video-embed.
 *
 * Remove the video embed template on this page, preventing the Vimeo
 * integration.
 */
function hideEmbed() {
  document.getElementById('video-embed-target').innerHTML = '';
  document.getElementById('video-confirm').style.display = 'block';
  document.getElementById('video-embed').style.display = 'none';
}

/**
 * Check cookie settings and initialize video embed on the page.
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
