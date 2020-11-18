import matplotlib.pyplot as plt

class Visualizer(object):
    def __init__(self):
        self.MY_COLORS  =["#2E2300","#DB9501","#375E97","#3F681C","#C05805"]
        
    def plot_t_shirt_data(self, data, x_axis_attribute, y_axis_attribute, equal_axis=False):
        """
        Plots t-shirt data

        :param data: DataFrame. The data frame for plotting.
        :param x_axis_attribute: String. The name of attribute from data frame to plot on x axis.
        :param y_axis_attribute: String. The name of attribute from data frame to plot on y axis.
        :param equal_axis: Boolean. Indicater whether to plot axis equal.
        """
        #take out x and y variables
        x=data[x_axis_attribute]
        y=data[y_axis_attribute]

        #plot basics
        fig=plt.figure()
        ax=fig.add_axes([0.1,0.1,0.8,0.8])

        #scatterplot
        ax.scatter(
                x=x,
                y=y,
                c=self.MY_COLORS[1],
                s=300,
                alpha=0.5,
                edgecolors=self.MY_COLORS[0]
        )

        #axis labeling
        ax.set_xlabel(x.name)
        ax.set_ylabel(y.name)
        ax.set_title("Initial Data Visualization")

        #setting axes
        if equal_axis:
            plt.axis("equal")
            
    def plot_clusters(self, x, y, labels):
        #plotting results
        fig_clust= plt.figure()
        ax = fig_clust.add_subplot()
        plt.scatter(x,y,c=labels,cmap='rainbow')
        
    def plot_score(self, x, y):
        fig = plt.figure()
        ax = fig.add_subplot()
        plt.plot(x, y, c=self.MY_COLORS[4])