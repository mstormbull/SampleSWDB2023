LowDimensionalDynamics = trialfactors#pca.fit_transform(trialfactors)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# load some test data for demonstration and plot a wireframe
xg = LowDimensionalDynamics[:,0]
yg = LowDimensionalDynamics[:,1]
zg = LowDimensionalDynamics[:,2]
ax.scatter(xg, yg, zg, c= np.linspace(0,len(xg),len(xg)) ,s=10, alpha = 0.5, marker='.', cmap='rainbow')
ax.set_xlabel('Modulatory Factor 1')
ax.set_xticks([-0,1])
ax.set_ylabel('Modulatory Factor 2')
ax.set_yticks([-0,1])
ax.set_zlabel('Modulatory Factor 3')
ax.set_zticks([-0,1])

# rotate the axes and update
for angle in range(0, 180):   # change this to fewer until you want to generate the whole rotation
	ax.view_init(30, angle)
	plt.savefig('RotatingTrialFactor' + str(angle).zfill(3), dpi = 300)