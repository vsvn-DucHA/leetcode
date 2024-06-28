# init-react

## Create project

```bash
npm create vite@latest
```

```bash
OK to process? (y) y
? Project name: vite-project
? Select a framework: React
? Select a variant: TypeScript + SWC
```

## Move to project and install library

```bash
cd vite-project
npm install   
```

### Eslint + Prettier

```bash
npm install eslint eslint-config-prettier eslint-plugin-prettier prettier --save-dev
```

Create .eslintrc.json by running:

```bash
npx eslint --init 
? How would you like to use ESLint?: check ... and find ...
? What type of modules does your project use?: javascript...
? Which framework does your project use?: React...
...
```