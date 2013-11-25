import csv

from .models import Parcel


def area_and_overlap_csv(filename='area_and_overlap.csv'):
    writer = csv.writer(open(filename, 'wb'))
    writer.writerow(['area (sq ft)', 'percent covered'])
    for parcel in Parcel.objects.all():
        pbo = parcel.parcelbuildingoverlap_set.all()[0]
        writer.writerow([parcel.calculate_area(), pbo.percent_parcel_covered])


def plot(filename='area_and_overlap.csv'):
    """
    Quick and dirty plotting of the data output by area_and_overlap_csv. Would
    likely want to do this more interactively, so consider this a record of
    plotting done and a starting point for more plotting.

    You will likely want to invoke ipython with the --matplotlib switch and
    the backend of your choice (we used tk):

        ipython --matplotlib tk

    """
    from matplotlib import pyplot
    from pylab import plt, show

    in_file = csv.reader(open(filename, 'rb'))
    areas = []
    overlaps = []
    for row in in_file:
        try:
            areas.append(float(row[0]))
            overlaps.append(float(row[1]))
        except Exception:
            print row[0], row[1]

    fig = pyplot.figure()
    ax = plt.gca()

    ax.set_ylabel('parcel area (sq ft, log)')
    ax.set_yscale('log')

    ax.set_xlabel('% of parcel that overlaps with building polygons')
    ax.plot(overlaps, areas, 'o', c='blue', alpha=0.05, markeredgecolor='none')
    show()
