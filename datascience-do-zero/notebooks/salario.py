salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

from collections import defaultdict

# as chaves são os anos, os valores são listas de salário por anos de experiência
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# as chaves são anos, cada valor é o salário médio assiciado ao npumero de anos de experiência
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print(average_salary_by_tenure)

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else: 
        return "more than five"
    
# as chaves são buckets de anos de experiência, os valores são as listas de salários associadas ao bucket em questão 
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures: 
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# as chaves são buckets de anos de experiência, os valores são a média salarial do bucket em questão
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}    

print(average_salary_by_bucket)

{'between two and five':
 61500.0, 'less than two':
 48000.0, 'more than five': 79166.66666666667}

# contas pagas
def predict_paid_or_unpaid(years_experience): 
    if years_experience < 3.0:
        return "paid"