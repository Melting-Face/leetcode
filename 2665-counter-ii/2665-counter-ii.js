/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  const init_value = init;
  
  let current_value = init_value;
  function increment() {
    current_value += 1;
    return current_value;
  }

  function decrement() {
    current_value -= 1;
    return current_value;
  }

  function reset() {
    current_value = init_value;
    return current_value;
  }

  return {
    increment,
    decrement,
    reset,
  }
};
/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */