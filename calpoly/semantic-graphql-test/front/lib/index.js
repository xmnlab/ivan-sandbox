"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const graphql_tag_1 = require("graphql-tag");
const apollo_boost_1 = require("apollo-boost");
const serviceUrl = 'http://localhost:3001/';
const node_fetch_1 = require("node-fetch");
// import { createHttpLink } from 'apollo-link-http';
/*
const link = createHttpLink({
  uri: serviceUrl, fetch: fetch
});
*/
/*
const defaultOptions = {
  watchQuery: {
    fetchPolicy: 'network-only',
    errorPolicy: 'ignore',
  },
  query: {
    fetchPolicy: 'network-only',
    errorPolicy: 'all',
  },
  mutate: {
    errorPolicy: 'all'
  }
}
*/
const client = new apollo_boost_1.default({
    uri: serviceUrl,
    credentials: 'same-origin',
    fetch: node_fetch_1.default
    // fetchOptions: defaultOptions
    // link: link
});
const query = graphql_tag_1.default `
    query __schema {
      types {
        name
      }
    }
`;
const variables = {};
client.query({
    query: query,
    variables: variables,
    fetchPolicy: 'network-only'
}).then(data => console.log(data))
    .catch(error => console.error(error));
