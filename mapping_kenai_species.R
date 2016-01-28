#This scripts is an adapted version of the one provided by Michael Fontaine
#for the course 'bioinformatics and computing for biologists'  at RuG.

setwd("~/NORTH_PACIFIC")
data <- read.table(file="Humpback Whale_2010.txt", header =TRUE)
#data <- read.table(file="Kenai.txt",header =TRUE)

attach(data) 

library(marmap)

#exLong <- 5

#xlim <- c(min(Long)-exLong,max(Long)+exLong)
#ylim <- c(min(Lat)-exLong,max(Lat)+exLong)

#getting data for map
bat <- getNOAA.bathy(lat1=55, lat2=63, lon=-145, lon2 = -155, keep= TRUE) #default res=4, keep means do not reload data but save.

blues <- c("lightsteelblue4","lightsteelblue3", "lightsteelblue2", "lightsteelblue1")
greys <- c(grey(0.6), grey(0.93), grey(0.99))


# plot data and coordinates of observations
plot(bat, image = TRUE, land = TRUE, lwd = 0.1, bpal = list(c(0, max(bat), greys), c(min(bat), 0, blues)))
plot(bat, lwd = 0.8, deep = 0, shallow = 0, step = 0, add = TRUE) # highlight coastline
points(Long, Lat, pch = 21, col = "black", bg = "yellow", cex = 1.3)

d#ev.copy2pdf(file="mapmarmap.pdf")

