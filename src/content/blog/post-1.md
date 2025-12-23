---
title: "How to build a web site with modern technology"
meta_title: ""
description: "this is meta description"
date: 2025-12-24T10:00:00Z
image: "/images/avatar-astro-dark.png"
categories: ["Web", "Development"]
author: "Steven Reiz"
tags: ["Astro", "VS Code", "WSL"]
draft: false
---

When setting out to create this latest revision of the company web site I wanted to move away from the tried and true (but tired) approach of using Wordpress. In particular I was looking for something that was more IDE-friendly, with content stored as Markdown and image files instead of in a database. This would make the workflow more developer- and AI-friendly. Preferably it should still support theming and support  Python-based customization. WYSIWYG editing was not a requirement, even though this would be easy to add with one of a number of Markdown-based CMS systems later if needed.

After reviewing a large number of options, including some low-code / AI-based tools, I settled on [Astro](https://astro.build/). It's a bit low-level but it is fully Open Source and has some great starter sites and themes available. It integrates well with a number of other front-end technologies, and it also didn't hurt that it produces modern static web sites that are very fast to load and use. The main downside is that customization is done in Typescript, not Python, but that's not unexpected for a front-end framework and for simple sites of limited relevance anyway. So far the experience with Astro has been great with quick development and editing due to its logical structure and live preview feature. It also has great community support.

## Creative Design

For the structure of the web site I selected a simple modern design, well-suited for startups and small companies, focused on a single page with a header, hero section and footer. Some smaller pages have been added as support, as well as a blog to add some expandability and SEO abilities. The [Astroplate](https://astro.build/themes/details/astroplate/) starter site / theme which I used for this is again Open Source.

## Content Generation

I was initally expecting to generate the bulk of the site, both text and images, in one go using AI in agent mode. While this is definitely possible (including Vibe-coding an Astro site around it), when starting to work on the site it turned out that setting up the Astro site was easy enough not to need much help. I also wanted to use WSL for running the Astro npm/yarn tooling to maintain a modicum of security, which would have made fully AI-driven development harder. 

Then when actually creating the content again it turned out to be easier to write the text by hand instead of making an AI do it. This left generating images for logos, illustrations etc. VS Code is great for managing a project like this (e.g. its remote/WSL support is flawless) but at least in the free tier of Github Copilot surprisingly none of the provided models support generating images. There are various ways of working around this, and I created an MCP server for this purpose to tie ComfyUI neatly into Copilot agent mode, but running it is a bit of a hassle. Instead I opted for using ComfyUI directly with its web UI and a few custom business-oriented workflows, then copying the results into VS Code.

All in all the project went smoothly, it was a good opportunity to learn some new tech and more satisfying to use this tooling than Wordpress. I will leave you to judge the resulting web site for yourself!
