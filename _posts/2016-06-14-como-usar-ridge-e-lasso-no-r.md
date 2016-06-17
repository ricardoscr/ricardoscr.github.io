---
layout: single
title: "Como usar Regressão Ridge e Lasso no R"
category: R
tags: [ridge, lasso, R]
comments: true
lang: pt-BR
mathjax: true
---

De uma maneira bem simples e direta ao ponto, após uma breve introdução dos métodos, vamos ver como executar no R Regressão Ridge e Lasso!

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

---

## Regressão Ridge no R

Regressão Ridge é um método de regularização que evita overfitting penalizando coeficientes grandes através da L2 Norm. Por isso, é também chamada de Regularização L2.

Em uma regressão linear, na prática isso implica em minimizar SQE (Soma dos Quadrados dos Resíduos) ou RSS (Residual Sum of Squares) somado à L2 Norm. Dessa forma, buscamos minimizar:

$$ RSS(\beta) + \lambda \sum_{j=1}^{p} \beta_j^2 $$

onde $$\lambda$$ é o parâmetro de tuning ou ajuste da penalidade, $$\beta_j$$ são os coeficientes estimados em quantidade $$p$$.

Para executar Regressão Ridge no R, faremos uso do pacote glmnet, desenvolvido pelos próprios criadores dos algoritmos.

```R
require(glmnet)
# Considerando que tenho um data frame de nome dados, sendo a primeira coluna a classe
x <- as.matrix(dados[,-1]) # Remove classe
y <- as.double(as.matrix(dados[, 1])) # Somente classe
set.seed(999)
cv.ridge <- cv.glmnet(x, y, family='binomial', alpha=0, parallel=TRUE, standardize=TRUE, type.measure='auc')
plot(cv.ridge)
cv.ridge$lambda.min
cv.ridge$lambda.1se
coef(cv.ridge, s=cv.ridge$lambda.min)
```

No código acima executamos regressão logística (perceba o family='binomial'), paralelizando (caso cluster ou cores tenham sido alocados previamente), internamente normalizando (é necessário para regularização mais adequada) e buscando observar medida de AUC (área sob curva ROC) nos resultados. Além disso, o método já executa 10-fold cross validation para escolher o melhor $$\lambda$$.

Ao final já passo alguns comandos úteis para verificação dos resultados, como exibição do gráfico dos resultados de AUC e valores de $$\lambda$$ mínimo (para AUC mínimo) e 1se (para AUC menor um desvio padrão do mínimo).

---

## Lasso no R

Agora vamos mexer com o Lasso! Lasso também é um método de regularização que evita overfitting penalizando coeficientes grandes, mas usa a L1 Norm. Por isso, é também chamada de Regularização L1.

Esse método tem como grande diferencial o fato de poder encolher alguns dos coeficientes a exatamente zero, realizando, portanto, uma seleção de atributos com a regularização.

Em uma regressão linear, na prática para o Lasso busca-se minimizar SQE (Soma dos Quadrados dos Resíduos) ou RSS (Residual Sum of Squares) somado à L1 Norm. Dessa forma, realizamos a minimização de:

$$ RSS(\beta) + \lambda \sum_{j=1}^{p} |\beta_j| $$

onde $$\lambda$$ é o parâmetro de tuning ou ajuste da penalidade, $$\beta_j$$ são os coeficientes estimados em quantidade $$p$$.

Para executar Lasso no R, faremos uso do pacote glmnet, desenvolvido pelos próprios criadores dos algoritmos.

```R
require(glmnet)
# Considerando que tenho um data frame de nome dados, sendo a primeira coluna a classe
x <- as.matrix(dados[,-1]) # Remove classe
y <- as.double(as.matrix(dados[, 1])) # Somente classe
cv.lasso <- cv.glmnet(x, y, family='binomial', alpha=1, parallel=TRUE, standardize=TRUE, type.measure='auc')
plot(cv.lasso)
plot(cv.lasso$glmnet.fit, xvar="lambda", label=TRUE)
cv.lasso$lambda.min
cv.lasso$lambda.1se
coef(cv.lasso, s=cv.lasso$lambda.min)
```

No código acima executamos regressão logística (perceba o family='binomial'), paralelizando (caso cluster ou cores tenham sido alocados previamente), internamente normalizando (é necessário para regularização mais adequada) e buscando observar medida de AUC (área sob curva ROC) nos resultados. Além disso, o método já executa 10-fold cross validation para escolher o melhor $$\lambda$$.

Ao final já passo alguns comandos úteis para verificação dos resultados, como exibição do gráfico dos resultados de AUC e valores de $$\lambda$$ mínimo (para AUC mínimo) e 1se (para AUC menor um desvio padrão do mínimo).

---

Como o post já ficou grande, em uma outra oportunidade falarei do Adaptive Lasso, uma evolução do Lasso que busca satisfazer a propriedade de Oráculo.


É isso, espero que tenha ficado claro!

Qualquer dúvida, sugestão: comente!
