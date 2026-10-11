const { DateTime } = require("luxon");

module.exports = function(eleventyConfig) {

  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("forms");
  eleventyConfig.addPassthroughCopy("_redirects");
  eleventyConfig.addGlobalData("currentYear", () => new Date().getFullYear());

  eleventyConfig.addFilter("postDate", (dateObj) => {
    return DateTime
      .fromJSDate(dateObj, { zone: "utc" })
      .toLocaleString(DateTime.DATE_MED);
  });

};