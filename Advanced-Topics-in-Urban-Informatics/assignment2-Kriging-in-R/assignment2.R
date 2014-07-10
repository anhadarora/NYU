#Codes for UK:
v <- variogram(num.incidents~population, dataset, cutoff=15000, width = 2000) 
vm <- vgm(psill = 0.05, model = "Exp", range = 15000, nugget = 0.01)
vmf <- fit.variogram(v,vm)
dev.new()
plot(v, pl=T, model = vmf)

#Codes for UK:
x.range <- range(dataset@coords[,1])
y.range <- range(dataset@coords[,2])
grd <- expand.grid(x=seq(from=x.range[1], to=x.range[2], by=500), y=seq(from=y.range[1], to=y.range[2], by=500) )
coordinates(grd) <- ~ x+y
gridded(grd) <- TRUE
krigpred <- krige(population~1, locations=dataset, newdata=grd, model=vmf)
a <- krigPred$var1.pred
grd <- expand.grid(x=seq(from=x.range[1], to=x.range[2], by=500), y=seq(from=y.range[1], to=y.range[2], by=500) )
grd[“population”] <- a
coordinates(grd) <- ~ x+y
gridded(grd) <- TRUE
krigPred <- krige(num.incidents~population, locations=dataset, newdata=grd, model=vmf)
print(plot(spplot(krigPred, "var1.pred", asp=1, col.regions=bpy.colors(64), main = "KED prediction")))

#Codes for UK:
print(plot(spplot(krigPred, "var1.var", asp=1, main = "KED prediction variance")))
