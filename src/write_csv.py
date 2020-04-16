import numpy as np
import itertools
import undx
import pcx
import sbx
import spx
import um
import de
import csv


def makeparams(low, high, dx):
    return(np.arange(low, high+0.001, dx).tolist())


# operator parameters
sbx_p = makeparams(0, 1, 0.25)
sbx_di = makeparams(0, 100, 10)
um_p = makeparams(0, 1, 0.25)
spx_eps = makeparams(0, 1, 0.25)
pcx_eta = makeparams(0, 1, 0.25)
pcx_zeta = makeparams(0, 1, 0.25)
undx_zeta = makeparams(0, 1, 0.25)
undx_eta = makeparams(0, 1, 0.25)

# operator parents
bounds = [(0, 10), (0, 10)]
SBX_parents = [(4, 5), (5, 7)]
DE_parents = [(3, 3), (4, 7), (4, 3), (6, 8)]
UM_parent = (3, 4)
PCX_parents = [(3, 3), (6, 3), (4.5, 6)]
UNDX_parents = [(3, 3), (6, 3), (4.5, 6)]
SPX_parents = [(3, 3), (6, 3), (4.5, 5)]

num_samples = 1000
operators = ["sbx", "um", "spx", "pcx", "undx"]
fields = ['x', 'y']

for i in range(len(operators)):
    op = operators[i]
    file_prefix = op + "_data_"

    if (op == "sbx"):
        for p in range(len(sbx_p)):
            first_suffix = str(sbx_p[p])
            for di in range(len(sbx_di)):
                second_suffix = str(sbx_di[di])
                filename = file_prefix + first_suffix + "_" + second_suffix + ".csv"
                f = open(filename, "w+")
                data = []
                for i in range(num_samples):
                    sol = sbx.sbx(SBX_parents, bounds,
                                  sbx_p[p], sbx_di[di])
                    data.append(sol[0])
                    data.append(sol[1])
                writer = csv.writer(f)
                writer.writerow(fields)
                writer.writerows(data)

    if (op == "um"):
        for p in range(len(um_p)):
            first_suffix = str(um_p[p])
            filename = file_prefix + first_suffix + ".csv"
            f = open(filename, "w+")
            data = []
            for i in range(num_samples):
                sol = um.um(UM_parent, bounds, um_p[p])
                data.append(sol)
            writer = csv.writer(f)
            writer.writerow(fields)
            writer.writerows(data)

    if (op == "spx"):
        for eps in range(len(spx_eps)):
            first_suffix = str(spx_eps[eps])
            filename = file_prefix + first_suffix + ".csv"
            f = open(filename, "w+")
            data = []
            for i in range(num_samples):
                sol = spx.spx(SPX_parents, spx_eps[eps])
                data.append(sol)
            writer = csv.writer(f)
            writer.writerow(fields)
            writer.writerows(data)

    if (op == "pcx"):
        for eta in range(len(pcx_eta)):
            first_suffix = str(pcx_eta[eta])
            for zeta in range(len(pcx_zeta)):
                second_suffix = str(pcx_zeta[zeta])
                filename = file_prefix + first_suffix + "_" + second_suffix + ".csv"
                f = open(filename, "w+")
                data = []
                for i in range(num_samples):
                    sol = pcx.pcx(PCX_parents, pcx_eta[eta], pcx_zeta[zeta])
                    data.append(sol)
                writer = csv.writer(f)
                writer.writerow(fields)
                writer.writerows(data)

    if (op == "undx"):
        for eta in range(len(undx_eta)):
            first_suffix = str(undx_eta[eta])
            for zeta in range(len(undx_zeta)):
                second_suffix = str(undx_zeta[zeta])
                filename = file_prefix + first_suffix + "_" + second_suffix + ".csv"
                f = open(filename, "w+")
                data = []
                for i in range(num_samples):
                    sol = undx.undx(
                        UNDX_parents, undx_zeta[zeta], undx_eta[eta])
                    data.append(sol)
                writer = csv.writer(f)
                writer.writerow(fields)
                writer.writerows(data)
