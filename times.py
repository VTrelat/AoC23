import json
from datetime import datetime, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def getIdList(data):
    return list(data['members'])


def getId(name, data):
    if name[:3] == "ID:":
        return name[3:]
    idList = getIdList(data)
    for i in idList:
        if name == data["members"][i]["name"]:
            return i
    return 0


def getNames(data):
    out = []
    idList = getIdList(data)
    for i in idList:
        name = data["members"][i]["name"]
        if name == None:
            name = "ID:" + i
        out.append(name)
    return out


def getName(id, data):
    return data["members"][id]["name"]


def getTimes(id, data):
    out = []

    for day in list(data["members"][id]["completion_day_level"].keys()):
        tmp = [int(day)]
        for part in sorted(
                list(data["members"][id]["completion_day_level"][day].keys())):
            tmp.append(data["members"][id]["completion_day_level"][day][part]
                       ["get_star_ts"])
        out.append(tmp)
    return sorted(out, key=lambda e: e[0])


def scaleTS(ts, unit):
    hour = datetime.fromtimestamp(ts).hour
    minute = datetime.fromtimestamp(ts).minute
    second = datetime.fromtimestamp(ts).second
    sec = int(unit == "sec")
    min = int(unit == "min")
    h = int(unit == "h")
    return (hour - 6) * (h + 60 * min + 3600 * sec) + minute * (
        h / 60 + min + sec * 60) + second * (h / 3600 + min / 60 + sec)


def getBest(data, k=1):
    ranks = []
    for id in getIdList(data):
        name = getName(id, data)
        if name == None:
            name = "ID:" + id
        ranks.append([name, data["members"][id]['local_score']])
    return [e[0] for e in sorted(ranks, key=lambda e: e[1])[::-1][0:k]]


def plot(name, data, disp=["Total"], unit="min"):
    times = getTimes(getId(name, data), data)
    for type in disp:
        if type == "1":
            plt.plot([e[0] for e in times],
                     [scaleTS(e[1], unit) for e in times],
                     '-o',
                     label=f"{name}: Part 1")
        if type == "2":
            x = list(filter(lambda e: len(e) == 3, times))
            plt.plot(
                [e[0] for e in x],
                [abs(scaleTS(e[2], unit) - scaleTS(e[1], unit)) for e in x],
                '-o',
                label=f"{name}: Part 2")
        if type == "Total":
            x = list(filter(lambda e: len(e) == 3, times))
            plt.plot(
                [e[0] for e in x],
                [abs(scaleTS(e[2], unit)) for e in x],
                "-o",
                label=f"{name}: total time",
            )
    plt.xlabel("Days")
    plt.ylabel(f"Time ({unit})")
    plt.legend()


def plot_avg(bests, data, disp="Total", unit="min", label="", curveType="-o"):
    days = [0 for _ in range(25)]
    counts = [0 for _ in range(25)]
    for name in bests:
        times = getTimes(getId(name, data), data)
        for time in times:
            if disp == "Total" and len(time) == 3:
                days[time[0] - 1] += scaleTS(time[2], unit)
                counts[time[0] - 1] += 1
            if disp == "1":
                days[time[0] - 1] += scaleTS(time[1], unit)
                counts[time[0] - 1] += 1
            if disp == "2" and len(time) == 3:
                days[time[0] - 1] += abs(
                    scaleTS(time[2], unit) - scaleTS(time[1], unit))
                counts[time[0] - 1] += 1
    while 0 in days:
        days.remove(0)
        counts.remove(0)
    for i in range(len(days)):
        days[i] /= counts[i]
    x = [i + 1 for i in range(len(days))]
    y = [e for e in days]
    if disp == "1":
        plt.plot(x, y, curveType, label="Part 1" + label)
        plt.title("Average total time for part 1")
    if disp == "2":
        plt.plot(x, y, curveType, label="Part 2" + label)
        plt.title("Average total time for part 2")
    if disp == "Total":
        plt.plot(x, y, curveType, label="Total" + label)
        plt.title("Average total time per day")
    plt.xlabel("Days")
    plt.ylabel(f"Time ({unit})")
    plt.legend()


def plot_fit(x, y, deg=3, curveType="--"):
    model = np.poly1d(np.polyfit(x, y, deg))

    line = np.linspace(x[0], x[-1], 100)
    plt.plot(line, model(line), curveType)


def model_avg(bests,
              data,
              deg,
              disp="Total",
              unit="min",
              label="",
              curveType="-o"):
    days = [0 for _ in range(25)]
    counts = [0 for _ in range(25)]
    for name in bests:
        times = getTimes(getId(name, data), data)
        for time in times:
            if disp == "Total" and len(time) == 3:
                days[time[0] - 1] += scaleTS(time[2], unit)
                counts[time[0] - 1] += 1
            if disp == "1":
                days[time[0] - 1] += scaleTS(time[1], unit)
                counts[time[0] - 1] += 1
            if disp == "2" and len(time) == 3:
                days[time[0] - 1] += abs(
                    scaleTS(time[2], unit) - scaleTS(time[1], unit))
                counts[time[0] - 1] += 1
    while 0 in days:
        days.remove(0)
        counts.remove(0)
    for i in range(len(days)):
        days[i] /= counts[i]
    x = [i + 1 for i in range(len(days))]
    y = [e for e in days]
    xnew = np.linspace(min(x), max(x), num=200, endpoint=True)

    if disp == "1":
        plot_fit(x, y, deg, curveType)
        plt.plot(x, y, label=label)
        plt.title("Average total time for part 1")
    if disp == "2":
        plot_fit(x, y, deg, curveType)
        plt.plot(x, y, label=label)
        plt.title("Average total time for part 2")
    if disp == "Total":
        plot_fit(x, y, deg, curveType)
        plt.plot(x, y, label=label)
        plt.title("Average total time per day")
    plt.xlabel("Days")
    plt.ylabel(f"Time ({unit})")
    plt.legend()


def plot_model_single(name, data, deg, disp=["Total"], unit="min"):
    times = getTimes(getId(name, data), data)
    for type in disp:
        if type == "1":
            plt.plot([e[0] for e in times],
                     [scaleTS(e[1], unit) for e in times],
                     '-o',
                     label=f"{name}: Part 1")
            plot_fit([e[0] for e in times],
                     [scaleTS(e[1], unit) for e in times], deg)
        if type == "2":
            x = list(filter(lambda e: len(e) == 3, times))
            plt.plot(
                [e[0] for e in x],
                [abs(scaleTS(e[2], unit) - scaleTS(e[1], unit)) for e in x],
                '-o',
                label=f"{name}: Part 2")
            plot_fit(
                [e[0] for e in x],
                [abs(scaleTS(e[2], unit) - scaleTS(e[1], unit))
                 for e in x], deg)
        if type == "Total":
            x = list(filter(lambda e: len(e) == 3, times))
            plt.plot(
                [e[0] for e in x],
                [abs(scaleTS(e[2], unit)) for e in x],
                "-o",
                label=f"{name}: total time",
            )
            plot_fit([e[0] for e in x], [abs(scaleTS(e[2], unit)) for e in x],
                     deg)
    plt.xlabel("Days")
    plt.ylabel(f"Time ({unit})")
    plt.legend()


json_file = open("times.json")
data = json.load(json_file)

# ############################## Cheaters ? ##############################
# # plt.figure(1)
# # plot("AdventOfCode Team3A", data, ["Total", "2"], unit="sec")
# # plot("ID:1666012", data, ["Total", "2"], unit="sec")

# cheaters = [
#     "marionlouis1", "martin ricouard", "Fish Sticks", "hugo-lafleur",
#     "MrJWinnefield", "AdventOfCode Team3A", "ID:1666012", "Comet92"
# ]
# # for cheater in cheaters:
# #     plot(cheater, data, "2", "sec")
# # plt.title("Potential cheaters")
# ########################################################################

# ############################# Display Bests ############################
# plt.figure(2)
# for name in getBest(data, 1):
#     plot(name, data, ["2"], unit="sec")
#     plot(name, data, ["1"], unit="sec")
#     plot(name, data, ["Total"], unit="sec")
# # plt.title("Best players")
# plt.xticks(range(1, 26))
# ########################################################################

# ############################ Average Time ##############################
# plt.figure(3)
# plt.subplot(311)
# plot_avg(getBest(data, 30), data, "2", label="(30 firsts)")
# plot_avg(getBest(data, 15), data, "2", label="(15 firsts)")
# plot_avg(getBest(data, 5), data, "2", label="(5 firsts)")
# plot_avg(getNames(data), data, "2", label="(all)", curveType='-')
# # model_avg(getBest(data, 10), data, "2", label="(10 firsts)", curveType="--")
# plt.xticks(range(1, 26))

# plt.subplot(312)
# plot_avg(getBest(data, 30), data, "1", label="(30 firsts)")
# plot_avg(getBest(data, 15), data, "1", label="(15 firsts)")
# plot_avg(getBest(data, 5), data, "1", label="(5 firsts)")
# plot_avg(getNames(data), data, "1", label="(all)", curveType='-')
# plt.xticks(range(1, 26))

# plt.subplot(313)
# plot_avg(getBest(data, 30), data, "Total", label="(30 firsts)")
# plot_avg(getBest(data, 15), data, "Total", label="(15 firsts)")
# plot_avg(getBest(data, 5), data, "Total", label="(5 firsts)")
# plot_avg(getNames(data), data, "Total", label="(all)", curveType="-")
# ########################################################################

# # plot('VTrelat', data, disp=["Total", "2"], unit="min")
# # plot('pemoreau', data, disp=["Total", "2"], unit="min")
# # plot('marceau-m', data, disp=["Total", "2"], unit="min")
# # plot_model_single("VTrelat", data, deg=7, disp=["Total", "2"], unit="sec")
# plt.show()

for name in getBest(data, 10):
    plot(name, data, ["2"], unit="min")
plt.show()
