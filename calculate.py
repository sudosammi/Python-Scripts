def calculate(numbers, operations):
  results = []
  for number in numbers:
    for operation in operations:
      result = number * operation
      results.append(result)
  return results

print(calculate([10, 20, 30], ["+", "-", "*"]))
