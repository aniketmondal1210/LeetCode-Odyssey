class EventEmitter {
    constructor() {
        this.events = {};
    }
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        // Initialize event array if it doesn't exist
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }
        
        // Add callback to the event
        this.events[eventName].push(callback);
        
        // Return unsubscribe object
        return {
            unsubscribe: () => {
                const index = this.events[eventName].indexOf(callback);
                if (index !== -1) {
                    this.events[eventName].splice(index, 1);
                }
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        // Return empty array if event has no subscribers
        if (!this.events[eventName]) {
            return [];
        }
        
        // Call all callbacks and collect results
        return this.events[eventName].map(callback => callback(...args));
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // 
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
