#!/usr/bin/node
'use strict';
let K = process.argv.length;
if (K === 2) {
    console.log('No argument');
} else if (K === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
