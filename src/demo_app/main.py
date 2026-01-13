import inspect
import pyspark.sql.udtf as u

print("Python:", __import__("sys").version)
print("UDTF file:", u.__file__)
print("AnalyzeArgument seists:", hasattr(u, "AnalyzeArgument"))

if hasattr(u, "AnalyzeArgument"):
    print("Defined in:", inspect.getsourcefile(u.AnalyzeArgument))
    print(inspect.getsource(u.AnalyzeArgument))
else:
    print("AnalyzeArgument NOT present")