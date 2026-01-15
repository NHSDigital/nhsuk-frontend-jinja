# Testing

## Requirements

To test the Jinja templates locally you'll need to:

- [set up git](https://help.github.com/articles/set-up-git/)
- [install Node.js](https://nodejs.org/en/)
  We recommend to use the [long-term support (LTS) version of Nodejs](https://nodejs.org/en/download/), rather than the latest beta version.
- install Python 3.11 or later

> Type `git --version` to check if git is installed. This should print a version number like "git version 2.18.0".

> Type `node -v` to check if Node is installed. This should print a version number like "v8.11.3".

## 1. Fork the repository

[Fork the repository](https://help.github.com/articles/fork-a-repo/) first, if you're an external contributor.

## 2. Clone the repository

You can clone the repository directly if you're a member of the [NHS Digital GitHub organisation](https://github.com/NHSDigital/)

```
git clone git@github.com:NHSDigital/nhsuk-frontend-jinja.git nhsuk-frontend-jinja
```

Otherwise you'll have to clone your own fork

```
git clone https://github.com/[Username]/nhsuk-frontend-jinja.git nhsuk-frontend-jinja
```

> Replace '[Username]' in the git clone command above with your own GitHub username.

## 3. Install dependencies

We use [node package manager (npm)](https://docs.npmjs.com/getting-started/what-is-npm) to manage javascript dependencies,
and [uv](https://docs.astral.sh/uv/) to manage python dependencies.

Whilst in the project directory you will need to install the dependencies listed in `package.json`

```
npm install
```

Then install the python dependencies:

```
uv install
```

## 4. Run the tests

```
uv run pytest
```

> The application will be available at [http://localhost:3000/nhsuk-frontend](http://localhost:3000/nhsuk-frontend).

---

Next: [Application architecture](application-architecture.md)
