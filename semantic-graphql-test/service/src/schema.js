const fs = require('fs');
const path = require('path');
const { GraphQLSchema, GraphQLObjectType, printSchema } = require('graphql');

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
const schema = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: 'Query',
    fields: {
      // Relay's favorite
      node: _.nodeField,
      dataset: {
        type: _.getObjectType('http://www.w3.org/wiki/WebSchemas/SchemaDotOrgSources#source_DatasetClass'),
        resolve: () => ({}),
      },
      person: {
        type: _.getObjectType('http://www.w3.org/wiki/WebSchemas/SchemaDotOrgSources#source_rNews'),
        resolve: () => ({}),
      },
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

module.exports = schema;

// Save schema in Schema language to disk
fs.writeFileSync(path.join(__dirname, '../lib/schema.graphql'), printSchema(schema));
console.log('Schema saved on disk');
