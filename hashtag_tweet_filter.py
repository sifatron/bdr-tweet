import re
import csv

        # do not include general words, e.g., napa, naturaldisaster
def hash_filter(input_file, output_file):
    r = re.compile(
        r"""
        earthquake | aftershock | aftershocks | foreshock | eathquake | eartquake | earthquakes | quake | bigearthquake | bayquake | earrhquake | majorearthquake | postearthquake | earthquakedamage | eathquakedamage | earthquakedamage2014 | 3amearthquake | earthquake2014 | earthquake14 | postearthquakeinspections
        | caearthquake | californiaearthquake | californiaearthquakes | CAearthquake | CAearthquakes | earthquakeCA | norcalearthquake | sfoearthquake | bayareaearthquake | norcaquake
        | napaquake | napaquakes | napaearthquake | southnapaquake | napashake | earthquakeinnapa | southnapaearthquake | eartquakenapa | sonomaquake | southnapearthquake | earthquakenapa | napaquake14 | napaquake2014 | westnapafault | earthquakeruinednapaplans | napastrong
        | prayfornapa | rebuildnapa  | staysafenapa | staystrongnapa | recovernapa | NapaEarthquake6
        | SanFranciscoearthquake | sfearthquake | bayareaquake | sfquake | earthquakesf | earthquakesanfrancisco | earthquakessf | sfeathquake | earthquakesf2014 | earthquakebayarea | sanfranquake2014
        | americancanyonquake | americancanyonearthquake | earthquakeamericancanyon | earthquakeamericancanyon | earthquakeinamericancanyon | prayforamericancanyon
        | myfirstquake | myfirstearthquake | my1stquake | earthquakebelt | earthquakesucks | earthquaketoday | hateearthquakes | pissoffearthquake | fuckyouearthquake | nomoreearthquakes | EarthquakeAt3am | thatwasafuckinghugeearthquake | noearthquakehere | noearthquakes | ItWasAnEarthquake | fearoftheearthquake | terroirquake | earthquakesfiresfloodsetc | caloforniaearthquake | postearthquakepost| earthquakepreparedness | survivedtheearthquake | earthquakereadiness | earthquakekit | earthquakeprobs | earthquakeproblems | haterofearthquakes | earthquakesurviving | firstquakeinnewhouse| earthquakesurvivor | August24EarthquakeSurvivor| sfearthquakewelcome | quakenoob | didntfeelanyearthquake | earthequakemode | isurvivedanearthquake |harvestearthquake | earthquakessuck | ihateearthquakes
        """,
        flags=re.I | re.X)
    disaster_tweets_count = 0
    with open(input_file, 'rU') as f:
        rd = csv.reader(f, delimiter=",")
        with open(output_file, "wb") as f2:
            for a in rd:
                arr = []
                #a = [x.strip() for x in line.split(',')]

                if len(a) > 5:
                    st = ""
                    for i in xrange(0, len(a) - 4):
                        if i == len(a) - 5:
                            st += a[i]
                        else:
                            st += a[i] + ", "
                    arr.append(st)
                    for i in xrange(len(a) - 4, len(a)):
                        arr.append(a[i])
                    a = []
                    a = arr
                if re.search(r, a[0]):
                    # print a[0]
                    f2.write(', '.join(a) + '\n')
                    disaster_tweets_count += 1
    print "Disaster related tweets: ", disaster_tweets_count