/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function (generator) {
  let cancelled = false;
  let resolveOuter, rejectOuter;
  const promise = new Promise((resolve, reject) => {
    resolveOuter = resolve;
    rejectOuter = reject;
  });

  const cancel = () => {
    cancelled = true;
    try {
      const result = generator.throw("Cancelled");
      if (result.done) {
        resolveOuter(result.value);
      } else {
        runGenerator(result.value);
      }
    } catch (e) {
      rejectOuter(e);
    }
  };

  const runGenerator = (promiseValue) => {
    if (cancelled) {
      try {
        const result = generator.throw("Cancelled");
        if (result.done) {
          resolveOuter(result.value);
        } else {
          runGenerator(result.value);
        }
      } catch (e) {
        rejectOuter(e);
      }
      return;
    }

    Promise.resolve(promiseValue)
      .then((value) => {
        try {
          const result = generator.next(value);
          if (result.done) {
            resolveOuter(result.value);
          } else {
            runGenerator(result.value);
          }
        } catch (e) {
          rejectOuter(e);
        }
      })
      .catch((err) => {
        try {
          const result = generator.throw(err);
          if (result.done) {
            resolveOuter(result.value);
          } else {
            runGenerator(result.value);
          }
        } catch (e) {
          rejectOuter(e);
        }
      });
  };

  try {
    const result = generator.next();
    if (result.done) {
      resolveOuter(result.value);
    } else {
      runGenerator(result.value);
    }
  } catch (e) {
    rejectOuter(e);
  }

  return [cancel, promise];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
