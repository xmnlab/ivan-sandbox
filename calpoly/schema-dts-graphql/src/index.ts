import { Person } from "schema-dts";

const p: Person = {
  "@type": "Person",
  name: "Eve",
  affiliation: {
    "@type": "School",
    name: "Nice School",
    alumni: [{
      "@type": "Person",
      name: "Joe"
    }]
  }
}
console.log(p);
