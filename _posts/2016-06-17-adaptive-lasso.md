---
layout: single
title: "Adaptive Lasso: O que é e como implementar no R"
category: R, en-us
tags: [ridge, lasso, adaptive lasso, R]
comments: true
lang: pt-BR
mathjax: true
---

Adaptive Lasso é uma evolução do Lasso. Vamos ver sucintamente como ele aprimora o Lasso e mostrar o código para executá-lo no R!

---

Lasso foi introduzido <a href='http://ricardoscr.github.io/como-usar-ridge-e-lasso-no-r.html'>neste outro post</a>, caso não conheça o método, por favor, leia-o <a href='http://ricardoscr.github.io/como-usar-ridge-e-lasso-no-r.html'>aqui</a> antes!

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

---

## Procedimento Oráculo

Antes de entramos no Adaptive Lasso é importante saber o que é um procedimento dito "Oráculo".

Um procedimento oráculo é aquele que possui as seguintes propriedades de oráculo:

- Identificar o subconjunto de variáveis dito verdadeiro; e
- Possuir taxa de predição/estimação ótima.

Há trabalhos <a href='http://www.stat.wisc.edu/~shao/stat992/zou2006.pdf'>(Zou 2006)</a> que evidenciam que o Lasso não possui as propriedades de oráculo. Vê-se que há casos onde um $$\lambda$$ que leva a taxa de predição ótima acaba com seleção de inconsistente de variáveis (por exemplo, com variáveis de ruído). Assim como há também casos de estimativas enviesadas para coeficientes grandes, levando a taxas de predição subótimas.

Portanto, vendo que o Lasso não é um procedimento oráculo, foi desenvolvido o Adaptive Lasso.

---

## Adaptive Lasso

O Adaptive Lasso é uma evolução do Lasso que possui as propriedades de oráculo (para uma escolha adequada de $$\lambda$$).

Adaptive Lasso, como método de regularização, evita overfitting penalizando coeficientes grandes. Além disso, possui o mesmo diferencial que o Lasso: pode encolher alguns dos coeficientes a exatamente zero, realizando, portanto, uma seleção de atributos com a regularização.

Em uma regressão linear, o Adaptive Lasso busca minimizar:

$$ RSS(\beta) + \lambda \sum_{j=1}^{p} \hat{\omega_j} |\beta_j| $$

onde $$\lambda$$ é o parâmetro de tuning ou ajuste da penalidade (definido através de 10-fold cross validation), $$\beta_j$$ são os coeficientes estimados em quantidade $$p$$. Além disso, vemos o $$\hat{\omega_j}$$, chamado Vetor Adaptativo de Pesos, o diferencial do Adaptive Lasso.

Com $$\hat{\omega_j}$$ acabamos realizando uma regularização diferente para cada coeficiente, ou seja, esse vetor adapta a penalidade para cada coeficiente. O Vetor Adaptativo de Pesos é definido como:

$$\hat{\omega_j} = \frac{1}{\left(|\hat{\beta_j}^{ini}|\right)^{\gamma}}$$

Na equação acima $$\hat{\beta_j}^{ini}$$ é uma estimativa inicial dos coeficientes, usualmente obtida através de <a href='http://ricardoscr.github.io/como-usar-ridge-e-lasso-no-r.html'>Regressão Ridge</a>. Assim o Adaptive lasso acaba penalizando mais coeficientes com estimativa inicial menor. 

Já o $$\gamma$$ do vetor adaptativo de pesos é uma constante positiva para ajuste do vetor adaptativo de pesos, sendo que os autores sugerem os valores possíveis de 0.5, 1 e 2.

---

## Adaptive Lasso no R

Para executar Adaptive Lasso no R, faremos uso do pacote glmnet, realizando a <a href='http://ricardoscr.github.io/como-usar-ridge-e-lasso-no-r.html'>Regressão Ridge</a> para criar o Vetor Adaptativo de Pesos, como mostrado a seguir.

```R
require(glmnet)
## Considerando que tenho um data frame de nome dados, sendo a primeira coluna a classe
x <- as.matrix(dados[,-1]) # Remove classe
y <- as.double(as.matrix(dados[, 1])) # Somente classe

## Ridge Regression para Vetor Adaptativo de Pesos
set.seed(999)
cv.ridge <- cv.glmnet(x, y, family='binomial', alpha=0, parallel=TRUE, standardize=TRUE)
w3 <- 1/abs(matrix(coef(cv.ridge, s=cv.ridge$lambda.min)
[, 1][2:(ncol(x)+1)] ))^1 ## Definindo gamma = 1
w3[w3[,1] == Inf] <- 999999999 ## Jogando valores estimados com Infinito para 999999999

## Adaptive Lasso
set.seed(999)
cv.lasso <- cv.glmnet(x, y, family='binomial', alpha=1, parallel=TRUE, standardize=TRUE, type.measure='auc', penalty.factor=w3)
plot(cv.lasso)
plot(cv.lasso$glmnet.fit, xvar="lambda", label=TRUE)
abline(v = log(cv.lasso$lambda.min))
abline(v = log(cv.lasso$lambda.1se))
coef(cv.lasso, s=cv.lasso$lambda.1se)
coef <- coef(cv.lasso, s='lambda.1se')
atributos_selecionados <- (coef@i[-1]+1) ## Considerando o data frame dados como mostrado no início
```

No código acima executamos regressão logística (perceba o family='binomial'), paralelizando (caso cluster ou cores tenham sido alocados previamente), internamente normalizando (é necessário para regularização mais adequada) e buscando observar medida de AUC (área sob curva ROC) nos resultados do Adaptive Lasso. Além disso, o método já executa 10-fold cross validation para escolher o melhor $$\lambda$$.

Fixando $$\gamma = 1$$ (útil variar entre os valores sugeridos: 0.5, 1 e 2), aplicamos o Vetor Adaptativo de Pesos através da função cv.glmnet com o argumento **penalty.factor**.

Ao final já passo alguns comandos úteis para verificação dos resultados, como exibição do gráfico dos resultados de AUC, valores de $$\lambda$$ mínimo (para AUC mínimo) e 1se (para AUC menor um desvio padrão do mínimo), além de gráfico mostrando a regularização feita.

---

É isso, Adaptive Lasso pode ser bem útil, então não hesite em testar!

Qualquer dúvida, sugestão: comente!
