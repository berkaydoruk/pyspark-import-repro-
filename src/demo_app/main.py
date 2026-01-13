import inspect
import pyspark.sql.udtf as u

print("Python OK")
print("UDTF file:", inspect.getsourcefile(u))

print("AnalyzeArgument exists:", hasattr(u, "AnalyzeArgument"))

if hasattr(u, "AnalyzeArgument"):
    print("Defined in:", inspect.getsourcefile(u.AnalyzeArgument))
    print(inspect.getsource(u.AnalyzeArgument))
