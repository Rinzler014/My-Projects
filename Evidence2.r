#Ricardo Adolfo Gonzalez Teran
#A01769410

#EVIDENCIA 2. PROYECTO INTEGRADOR

evidencia <- function(){

  #Inciso 2. Analisar las secuencias y encontrar su longitud
  
  secuencias <- c( "JX869059", "AY508724", "MN908947", "AY390556", "AY278489", "MN985325","AY485277","MT292571")
  
  virus_sequences <- read.GenBank(secuencias)
  str(virus_sequences)
  
  #Inciso 3. Graficar las bases de ADN y comparar cada una de cada secuencia
  
  cantidades <- c("30119", "29732", "29903", "29760", "29757", "29882", "29741", "29782")
  
  data <- data.frame(secuencias, cantidades)
  ggplot(data, aes(fill=secuencias,y=cantidades,x=secuencias)) + geom_bar(position="dodge", stat="identity")
  
  #Extras-----------------------------------------------------
  
  #Creacion de un arbol filogenetico con las librerias de APE, Biostirngs y GGtree
  
  virus_sequences <- ape::read.GenBank(secuencias)
  str(virus_sequences)
  
  attributes(virus_sequences)
  names(virus_sequences)
  attr(virus_sequences, "species")
  
  ape::write.dna(virus_sequences,  file ="virus_seqs.fasta", format = "fasta", append =
                   FALSE, nbcol = 6, colsep = " ", colw = 10)
  
  
  # alinear las secuencias con respecto a virus_seq_not_align
  
  
  virus_seq_not_align <- OrientNucleotides(virus_seq_not_align)
  
  virus_seq_align <- AlignSeqs(virus_seq_not_align)
  
  
  # Se guarda el resultado con biostrings 
  
  writeXStringSet(virus_seq_align, file="virus_seq_align.fasta")
  
  virus_aligned <- read.alignment("virus_seq_align.fasta", format = "fasta")
  
  
  # con seqinr se genera una matriz de distancia donde sombras más oscuras de gris 
  #significan una mayor distancia
  
  matriz_distancia <- dist.alignment(virus_aligned, matrix = "similarity")
  
  temp <- as.data.frame(as.matrix(matriz_distancia))
  table.paint(temp, cleg=0, clabel.row=.5, clabel.col=.5) + scale_color_viridis()
  
  # Creación del árbol con el paquete ape
  
  virus_tree <- nj(matriz_distancia)
  class(virus_tree) 
  virus_tree <- ladderize(virus_tree)
  
  # visualizar el arbol 
  
  plot(virus_tree, cex = 0.6)
  title("Arbol Filogenético de las secuencias")


}

graficas <- function(){
  
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
  
  
  
}


evidencia()
graficas()