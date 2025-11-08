var TimeLimitedCache = function() {
    // Map: key -> { value: number, timeoutId: Timeout }
    this.map = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const existing = this.map.get(key);
    const existedAndUnexpired = existing !== undefined;

    // If key existed, clear previous timeout (we'll reschedule)
    if (existing) {
        clearTimeout(existing.timeoutId);
    }

    // Schedule removal after duration milliseconds
    const timeoutId = setTimeout(() => {
        // only delete the key if it's the same entry (defensive)
        const entry = this.map.get(key);
        if (entry && entry.timeoutId === timeoutId) {
            this.map.delete(key);
        }
    }, duration);

    // Store/overwrite the entry
    this.map.set(key, { value: value, timeoutId: timeoutId });

    return !!existedAndUnexpired;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const entry = this.map.get(key);
    return entry ? entry.value : -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.map.size;
};
