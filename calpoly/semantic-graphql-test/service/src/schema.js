const fs = require('fs');
const path = require('path');
const { GraphQLSchema, GraphQLObjectType } = require('graphql');

// Apply custom fields before anything else
require('./customFields');

const _ = require('./graph');

// Build mutations from directory
const mutationFields = {};
const mutationDir = path.join(__dirname, './mutations/');

fs.readdirSync(mutationDir).forEach(fileName => {
  mutationFields[fileName.split('.js')[0]] = require(mutationDir + fileName);
});

// Build schema
module.exports = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: 'Query',
    fields: {
      // Relay's favorite
      node: _.nodeField,
      // Helpers for common app resources
      // Viewer's data entry point
      /*
      viewer: {
        resolve: (source, args, { viewer }) => viewer,
      },*/
    },
  }) /*,
  mutation: new GraphQLObjectType({
    name: 'Mutation',
    fields: mutationFields,
  }),*/
});

