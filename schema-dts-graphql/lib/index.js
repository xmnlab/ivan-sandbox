"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const p = {
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
};
console.log(p);
