library(seqinr)
library(ggplot2)

variante_1 <- read.fasta("JX869059.fasta")
variante_2 <- read.fasta("AY508724.fasta")
variante_3 <- read.fasta("MN908947.fasta")
variante_4 <- read.fasta("AY390556.fasta")
variante_5 <- read.fasta("AY278489.fasta")
variante_6 <- read.fasta("MN985325.fasta")
variante_7 <- read.fasta("AY485277.fasta")
variante_8 <- read.fasta("MT292571.fasta")

v1_plot <- count(variante_1[[1]], 1)
v1_plot

v2_plot <- count(variante_2[[1]], 1)
v2_plot

v3_plot <- count(variante_3[[1]], 1)
v3_plot

v4_plot <- count(variante_4[[1]], 1)
v4_plot

v5_plot <- count(variante_5[[1]], 1)
v5_plot

v6_plot <- count(variante_6[[1]], 1)
v6_plot

v7_plot <- count(variante_7[[1]], 1)
v7_plot

v8_plot <- count(variante_8[[1]], 1)
v8_plot

#sequencesss <- c(rep("B1.52" , 4) , rep("B1.1.7" , 4) , rep("P.1" , 4))
#nucleotidos <- rep(c("a" , "c" , "g" , "t") , 3)

secuencias <- c( rep("JX869059", 4), rep("AY508724", 4), rep("MN908947", 4), rep("AY390556", 4), rep("AY278489", 4), rep("MN985325", 4), rep("AY485277", 4), rep("MT292571", 4))
Nucleotidos <- c("Adeninas", "Citosinas", "Guaninas", "Timinas")
Cantidades <- c(v1_plot , v2_plot , v3_plot, v4_plot, v5_plot, v6_plot, v7_plot, v8_plot)

data <- data.frame(secuencias,Nucleotidos,Cantidades)

ggplot(data, aes(fill=Nucleotidos,y=Cantidades,x=secuencias)) + 
  geom_bar(position="dodge", stat="identity")

