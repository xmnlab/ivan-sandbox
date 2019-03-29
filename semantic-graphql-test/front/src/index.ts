import gql from 'graphql-tag';
import ApolloClient from 'apollo-boost';

const serviceUrl = 'http://localhost:3001/';

import fetch from 'node-fetch';
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

const client = new ApolloClient({
  uri: serviceUrl,
  credentials: 'same-origin', // See: https://www.apollographql.com/docs/react/recipes/authentication.html
  fetch: fetch
  // fetchOptions: defaultOptions
  // link: link
});

const query = gql`
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

