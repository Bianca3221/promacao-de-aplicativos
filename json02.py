import json
open('notas.json','w').close()


aluno = {
        "matematica" : 8.5,
        "portugues" : 9.0, 
        "soma" : 0 
    }


soma = aluno["matematica"] + aluno["portugues"]
aluno["soma"] = soma
print(f"soma das notas :{soma}")


with open("notas.json", 'a', encoding="utf-8") as arquivo:
    json.dump(aluno, arquivo, ensure_ascii=False)

