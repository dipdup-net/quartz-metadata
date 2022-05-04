# Ubisoft Quartz GQL client

[![npm version](https://badge.fury.io/js/%40dipdup%2Fquartz.svg)](https://badge.fury.io/js/%40dipdup%2Fquartz)
[![Made With](https://img.shields.io/badge/made%20with-dipdup-blue.svg?)](https://dipdup.net)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Autogenerated typed SDK for Ubisoft Quartz NFTs with a built-in GQL client.

## Installation

```
npm i @dipdup/quartz
```

## Usage

First of all you need to create an instance of Quartz metadata client:
```js
import { createClient } from '@dipdup/quartz'

const client = createClient({
    url: 'http://quartz.dipdup.net/v1/graphql',
    subscription: {
        url: "wss://quartz.dipdup.net/v1/graphql"
    }
});
```

#### Query

```js
import { everything } from '@dipdup/quartz'

client.chain.query
    .token_metadata({
        where: {
            token_id: { _eq: "101252" }
        }
    })
    .get({ ...everything })
    .then(res => console.log)
```

## Release

Make sure you have bumped and comitted the package version.

```
npm i
npm run build
npm publish --access public
```