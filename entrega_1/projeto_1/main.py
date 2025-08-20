import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

print("1° Teste: lista [0,1,2,3,4,5,6,7,8]")
try:
        result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
    print("Resultado:")
    for key, value in result.items():
        print(f"  '{key}': {value}")
         print("Teste realizado com sucesso!\n")
except Exception as e:
    print(f"Foi encontrado um erro: {e}\n")


main(module='test_module', exit=False)