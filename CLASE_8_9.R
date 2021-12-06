#PREVIAMENTE INSTALA TU PAQUETERIA 

#1. biostrings
#2. Seqinr
#3.adegenet/ade4
#4.ape
#5.ggtree
#6.DECIPHER
#7. viridis
#8. ggplot2
#9.gridextra
#10 BiocGenerics  
#11 BiocManager se utiliza para instalar programas que no estan disponibles 
#por la versión

#crear un vector combinado con las secuencias e identificadores de cada fasta

virus <- c( "JX869059", "AY508724", "MN908947", "AY390556", "AY278489", "MN985325","AY485277","MT292571")
print(virus)

#Leer los atributos de las secuencias
#Con ape se leen las secuencias con los identificadores del GenBank, se asigna 
#un nombre nuevo y se crea un archivo virtual.
#Le asignamos un nuevo nombre al vector combinado para dar un nuevo atributo
#y formato fasta con las secuecias combinadas 
#En el codigo las "especies" son los nombres y numero de nuestras secuencias

virus_sequences <- ape::read.GenBank(virus)
str(virus_sequences)

attributes(virus_sequences)
names(virus_sequences)
attr(virus_sequences, "species")

ape::write.dna(virus_sequences,  file ="virus_seqs.fasta", format = "fasta", append =
            FALSE, nbcol = 6, colsep = " ", colw = 10)



#visualizar el arreglo de las secuencias sin alinear con biostrings

virus_seq_not_align <- readDNAStringSet("virus_seqs.fasta", format = "fasta")
virus_seq_not_align


# alinear las secuencias con respecto a virus_seq_not_align


virus_seq_not_align <- OrientNucleotides(virus_seq_not_align)

virus_seq_align <- AlignSeqs(virus_seq_not_align)


#visualizar con DECIPHER

BrowseSeqs(virus_seq_align, highlight=0)


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
title("A Novel Coronavirus from Patients with Pneumonia in China, 2019")

#visualizar diferentes formas del arbol de distancias con ggtree (ggplot2)


ggtree(virus_tree)
ggtree(virus_tree, layout="slanted") 
ggtree(virus_tree, layout="circular")
ggtree(virus_tree, layout="fan", open.angle=120)
ggtree(virus_tree, layout="equal_angle")
ggtree(virus_tree, branch.length='none')
ggtree(virus_tree, branch.length='none', layout='circular')
ggtree(virus_tree ) + geom_tiplab()

#para citar 

citation("dplyr")

