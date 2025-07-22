---
title: Hugo Explorer
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Hugo Explorer

A Visual Studio Code extension that provides a specialized file explorer for Hugo projects,
displaying content ordered by the `weight` parameter in markdown front matter while maintaining complete Explorer functionality.

## Features

✅ **Hugo Weight-Based Sorting**: Automatically orders files and directories based on the `weight` parameter in YAML front matter
✅ **Complete Explorer Functionality**: All native VS Code Explorer features including context menus, drag-and-drop, and file operations
✅ **Multi-Workspace Support**: Works seamlessly with multiple workspace folders
✅ **Drag-and-Drop File Moving**: Move files and folders while maintaining Hugo ordering
✅ **Native Context Menus**: Full right-click context menus identical to the native Explorer
✅ **Hugo _index.md Support**: Recognizes `_index.md` files for directory weight ordering
✅ **Fallback Alphabetical Sorting**: Items without weight are sorted alphabetically

## Installation

1. Download the VSIX file from here: [Hugo Explorer VSIX](../../_static/public/hugo-explorer-1.0.2.vsix)
2. Install via the command `Extensions: Install from VSIX...`

## Usage

1. Open a Hugo project in VS Code
2. Look for the "Hugo Explorer" icon in the Activity Bar (left sidebar)
3. The extension automatically detects and orders your Hugo content by weight
4. Use most of the same operations as the native Explorer:
   - Right-click for context menus
   - Drag and drop to move files
   - Create, rename, delete files and folders
   - Copy/paste operations.
5. To add a Workspace folder to the Hugo Explorer, either
   - Add it in the standard Explorer view (it will appear in the Hugo Explorer view automatically), or
   - Click on the "..." menu at the top of the Hugo Explorer to add folders from the Hugo Explorer view.
6. To remove a Workspace folder from the Hugo Explorer, either
   - Remove it from the standard Explorer view (it will be removed from the Hugo Explorer view automatically), or
   - Right-click on the folder in the Hugo Explorer view and select "Remove Folder".

## How It Works

* The extension finds the `content` folder in the root of your Hugo project.
* It places that folder at the top of the Hugo Explorer view.
* Within that folder it orders all files and directories as follows:
  - Directories are ordered by the `weight` parameter in the front matter of their `_index.md` file.
  - Files are ordered by the `weight` parameter in their front matter.
  - Items with lower (non-zero, positive) weights are placed before items with higher (non-zero, positive) weights.
  - If no weight is specified, files and directories are assumed to have a zero weight and are placed after all other items with a weight.
  - Items with the same weight are sorted alphabetically by their filename with directories sorted before files.
* Outside the `content` folder all files and folders are sorted as they are in the in the standard VS Code Explorer view, by their filename, with directories sorted before files.

The `weight` is defined in the front matter of the markdown files, which is a YAML block at the top of each file.

## Requirements

- Visual Studio Code 1.97.0 or higher
- Works with any Hugo project structure

