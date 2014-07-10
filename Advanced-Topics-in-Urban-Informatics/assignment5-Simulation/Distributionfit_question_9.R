setwd("C:/users/gang/desktop")
library(MASS)

data<-read.delim("Output_question_9.txt",header=TRUE,sep=",")
data <- as.numeric(data$delay)

fitdistr(data, "gamma")
fitdistr(data, "weibull")

# Gamma fit
x <- data
h<-hist(x, breaks=seq(min(x),max(x),l= 15), main="Histogram with Gamma Curve") 
h$counts
xfit<-seq(min(x),max(x),length=40) 
yfit<-dgamma(xfit, shape= 3.86053449 , rate = 0.16959953)
yfit <- yfit*diff(h$mids[1:2])*length(x) 
lines(xfit, yfit, col="red", lwd=1)

p<-c((pgamma(11.715438,shape= 3.86053449 , rate = 0.16959953)-pgamma(4.983341,shape= 3.86053449 , rate = 0.16959953)), 
     (pgamma(18.447535,shape= 3.86053449 , rate = 0.16959953)-pgamma(11.715438,shape= 3.86053449 , rate = 0.16959953)), 
     (pgamma(25.179632,shape= 3.86053449 , rate = 0.16959953)-pgamma(18.447535,shape= 3.86053449 , rate = 0.16959953)), 
     (pgamma(31.911729,shape= 3.86053449 , rate = 0.16959953)-pgamma(25.179632,shape= 3.86053449 , rate = 0.16959953)), 
     (pgamma(38.643826,shape= 3.86053449 , rate = 0.16959953)-pgamma(31.911729,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(45.375922,shape= 3.86053449 , rate = 0.16959953)-pgamma(38.643826,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(52.108019,shape= 3.86053449 , rate = 0.16959953)-pgamma(45.375922,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(58.840116,shape= 3.86053449 , rate = 0.16959953)-pgamma(52.108019,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(65.572213,shape= 3.86053449 , rate = 0.16959953)-pgamma(58.840116,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(72.304310,shape= 3.86053449 , rate = 0.16959953)-pgamma(65.572213,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(79.036407,shape= 3.86053449 , rate = 0.16959953)-pgamma(72.304310,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(85.768503,shape= 3.86053449 , rate = 0.16959953)-pgamma(79.036407,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(92.500600,shape= 3.86053449 , rate = 0.16959953)-pgamma(85.768503,shape= 3.86053449 , rate = 0.16959953)),
     (pgamma(99.232697,shape= 3.86053449 , rate = 0.16959953)-pgamma(92.500600,shape= 3.86053449 , rate = 0.16959953))) 

p<- p/sum(p)
qq = h$count/sum(h$count)
aa <- p-qq
plot( c(1:14), aa,col= 'red', lwd = 1, type = "b")

x.teo<-rgamma(n=10000,shape= 3.86053449 , rate = 0.16959953) ## theorical quantiles from a 
qqplot(x.teo,data,main="QQ-plot Gamma") ## QQ-plot 
abline(0,1) ## a 45-degree reference line is plotted 

mm <- vector()
data.cut <- cut(data, breaks = c( 4.983341, 11.715438, 18.447535, 25.179632, 31.911729, 38.643826, 45.375922, 52.108019, 58.840116, 65.572213, 72.304310 ,79.036407 ,85.768503 ,92.500600 ,99.232698))
table(data.cut)                        
for(i in 1:14) mm[i]<- table(data.cut)[[i]]
ks.test( mm, "pgamma", shape= 3.86053449 , rate = 0.16959953, alternative = "greater")


# Weibull fit
x <- data
h<-hist(x, breaks=seq(min(x),max(x),l= 15), main="Histogram with Weibull Curve") 
h$counts
xfit<-seq(min(x),max(x),length=40) 
yfit<-dweibull(xfit, shape= 1.95160124 , scale = 25.83152661)
yfit <- yfit*diff(h$mids[1:2])*length(x) 
lines(xfit, yfit, col="red", lwd=1)


p<-c((pweibull(11.715438,shape= 1.95160124 , scale = 25.83152661)-pweibull(4.983341,shape= 1.95160124 , scale = 25.83152661)), 
     (pweibull(18.447535,shape= 1.95160124 , scale = 25.83152661)-pweibull(11.715438,shape= 1.95160124 , scale = 25.83152661)), 
     (pweibull(25.179632,shape= 1.95160124 , scale = 25.83152661)-pweibull(18.447535,shape= 1.95160124 , scale = 25.83152661)), 
     (pweibull(31.911729,shape= 1.95160124 , scale = 25.83152661)-pweibull(25.179632,shape= 1.95160124 , scale = 25.83152661)), 
     (pweibull(38.643826,shape= 1.95160124 , scale = 25.83152661)-pweibull(31.911729,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(45.375922,shape= 1.95160124 , scale = 25.83152661)-pweibull(38.643826,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(52.108019,shape= 1.95160124 , scale = 25.83152661)-pweibull(45.375922,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(58.840116,shape= 1.95160124 , scale = 25.83152661)-pweibull(52.108019,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(65.572213,shape= 1.95160124 , scale = 25.83152661)-pweibull(58.840116,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(72.304310,shape= 1.95160124 , scale = 25.83152661)-pweibull(65.572213,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(79.036407,shape= 1.95160124 , scale = 25.83152661)-pweibull(72.304310,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(85.768503,shape= 1.95160124 , scale = 25.83152661)-pweibull(79.036407,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(92.500600,shape= 1.95160124 , scale = 25.83152661)-pweibull(85.768503,shape= 1.95160124 , scale = 25.83152661)),
     (pweibull(99.232697,shape= 1.95160124 , scale = 25.83152661)-pweibull(92.500600,shape= 1.95160124 , scale = 25.83152661))) 

p<- p/sum(p)
qq = h$count/sum(h$count)
aa <- p-qq
plot( c(1:14), aa,col= 'red', lwd = 1, type = "b")

x.teo<-rweibull(n=10000,shape= 1.95160124 , scale = 25.83152661) ## theorical quantiles from a 
qqplot(x.teo,data,main="QQ-plot Weibull") ## QQ-plot 
abline(0,1) ## a 45-degree reference line is plotted 


mm <- vector()
data.cut <- cut(data, breaks = c( 4.983341, 11.715438, 18.447535, 25.179632, 31.911729, 38.643826, 45.375922, 52.108019, 58.840116, 65.572213, 72.304310 ,79.036407 ,85.768503 ,92.500600 ,99.232698))
table(data.cut)                        
for(i in 1:14) mm[i]<- table(data.cut)[[i]]
ks.test( mm, "pweibull",shape= 1.95160124 , scale = 25.83152661, alternative = "greater")

