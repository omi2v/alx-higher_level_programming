#!/usr/bin/node
let argCount = process.argv.length - 2;
if (argCount < 1 )
{
console.log('No argument');
}
if (argCount > 1)
{
console.log('Argument found');
}
else
{
console.log('Arguments found');
}	
