import random
import numpy

class City:
    """
    Creates the city as a pair of x and y coordiantes.
    Can calculate the distance between two cities
    """
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord


    def get_distance(self, city):
        x_distance = abs(self.x_coord - city.x_coord)
        y_distance = abs(self.y_coord - city.y_coord)
        return numpy.sqrt(x_distance**2 + y_distance**2)


class Individual:
    """
    Creates an individual by creating its own gene sequence
    Calculates the fitness quality of an individual
    """
    def __init__(self, gene_pool=None, gene_sequence=None):
        self.gene_pool = gene_pool
        if gene_sequence:
            self.gene_sequence = gene_sequence
        else:
            self.gene_sequence = self.create_gene_sequence()
        self.fitness = self.determine_fitness()


    def create_gene_sequence(self):
        """
        Creates one individual by randomly taking a sample from the gene pool and adding the home city on the end
        """
        gene_sequence = random.sample(list(self.gene_pool), len(self.gene_pool))
        gene_sequence += gene_sequence[0]
        self.gene_sequence = gene_sequence
        return gene_sequence


    def determine_fitness(self):
        """
        Calculate the distance between each city. The total distance is the fitness value
        """
        total_distance = 0
        gene_sequence = self.get_gene_sequence()
        for gene in range(len(gene_sequence) - 1):
            city_1 = self.gene_pool[gene_sequence[gene]]
            city_2 = self.gene_pool[gene_sequence[gene + 1]]
            total_distance += city_1.get_distance(city_2)

        self.fitness = total_distance

        return total_distance


    # def create_fitness(self):
    #     if self.fitness == 0:
    #         fitness = determine_fitness(self.gene_sequence, self.gene_pool)
    #         self.fitness = fitness
    #     return self.fitness


    def get_gene_sequence(self):
        return self.gene_sequence


    def get_fitness(self):
        return self.fitness