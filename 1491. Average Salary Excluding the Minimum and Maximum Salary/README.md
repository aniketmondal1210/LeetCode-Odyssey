You are given an array of **unique integers** `salary` where `salary[i]` is the salary of the *i-th* employee.

Return the **average salary** of employees excluding the **minimum** and **maximum** salary.  
Answers within `10^-5` of the actual answer will be accepted.

---

### Example 1:

**Input:**  
`salary = [4000,3000,1000,2000]`  
**Output:**  
`2500.00000`  
**Explanation:**  
Minimum salary is `1000` and maximum salary is `4000`.  
Average salary excluding min and max is `(2000 + 3000) / 2 = 2500`.

---

### Example 2:

**Input:**  
`salary = [1000,2000,3000]`  
**Output:**  
`2000.00000`  
**Explanation:**  
Minimum salary is `1000` and maximum salary is `3000`.  
Average salary excluding min and max is `(2000) / 1 = 2000`.

---

### Constraints:

- `3 <= salary.length <= 100`
- `1000 <= salary[i] <= 10^6`
- All elements of `salary` are **unique**
