# Installation Guide

[Back Home](/)

## Automatic Installation

We recommend starting a new Next.js app using `create-next-app`, which sets up everything automatically for you.

To create a project, run: `npx create-next-app@latest`

After the prompts, `create-next-app` will create a folder with your project name and install the required dependencies.

If you're new to Next.js, see the *project structure* docs for an overview of all the possible files and folders in your application.

## Manual Installation

To manually create a new Next.js app, install the required packages:

`npm install next@latest react@latest react-dom@latest`

### Open your `package.json` file and add the following `scripts`:

These scripts refer to the different stages of developing an application:

`dev`: runs `next dev` to start Next.js in development mode.
`build`: runs `next build` to build the application for production usage.
`start`: runs `next start` to start a Next.js production server.
`lint`: runs `next lint` to set up Next.js' built-in ESLint configuration.