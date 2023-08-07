async function doThis() {
  console.log('Doing this, wait please');
  await new Promise((resolve) => setTimeout(resolve, 1000));
  console.log('Do this');
}

doThis();
console.log('Doing something else while do_this is running!');
