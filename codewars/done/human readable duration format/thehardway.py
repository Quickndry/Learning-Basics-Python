def format_duration(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365
    
    if seconds == 0:
        return "now"

    if years < 1:
        if days < 1:
            if hours < 1:
                if minutes < 1:
                    return "{s} {ss}".format(s = seconds, \
                        ss = "seconds" if int(seconds) > 1 else "second")
                
                elif minutes == int(minutes):
                    return "{mi} {min}".format(mi = int(minutes), \
                        min = "minutes" if int(minutes) > 1 else "minute")
                
                else:
                    seconds_r = (minutes - int(minutes)) * 60
                    return "{mi} {min} and {s} {ss}".format(mi = int(minutes), \
                        min = "minutes" if int(minutes) > 1 else "minute", s = int(seconds_r), \
                            ss = "seconds" if int(seconds) > 1 else "second")

            elif hours == int(hours):
                return "{h} {ho}".format(h = int(hours), \
                    ho = "hours" if int(hours) > 1 else "hour")
            
            else:
                minutes_r = (hours - int(hours)) * 60
                if minutes_r < 1:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{h} {ho} and {s} {ss}".format(h = int(hours), \
                        ho = "hours" if int(hours) > 1 else "hour", s = int(seconds_r), \
                            ss = "seconds" if int(seconds_r) > 1 else "second")

                elif minutes_r == int(minutes_r):
                    return "{h} {ho} and {mi} {min}".format(h = int(hours), \
                        ho = "hours" if int(hours) > 1 else "hour", mi = int(minutes_r), \
                            min = "minutes" if int(minutes_r) > 1 else "minute")

                else:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{h} {ho}, {mi} {min} and {s} {ss}".format(h = int(hours), \
                        ho = "hours" if int(hours) > 1 else "hour", mi = int(minutes_r), \
                            min = "minutes" if int(minutes_r) > 1 else "minute", s = round(seconds_r), \
                                ss = "seconds" if round(seconds_r) > 1 else "second")


        elif days == int(days):
            return "{d} {da}.".format(d = int(days), \
                da = "days" if int(days) > 1 else "day")

        else:
            hours_r = (days - int(days)) * 24
            if hours_r < 1:
                minutes_r = (hours_r - int(hours_r)) * 60
                if minutes_r < 1:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{d} {da} and {s} {ss}".format(d = int(days), \
                        da = "days" if int(days) > 1 else "day", s = round(seconds_r, \
                            ss = "seconds" if round(seconds_r) > 1 else "second"))
                elif minutes_r == int(minutes_r):
                    return "{d} {da} and {mi} {min}".format(d = int(days), \
                        da = "days" if int(days) > 1 else "day", mi = int(minutes_r), \
                            min = "minutes" if int(minutes_r) > 1 else "minute")
                else:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{d} {da}, {mi} {min} and {s} {ss}".format(d = int(days), \
                        da = "days" if int(days) > 1 else "day", mi = int(minutes_r), \
                            min = "minutes" if int(minutes_r) > 1 else "minute", s = round(seconds_r), \
                                ss = "seconds" if round(seconds_r) > 1 else "second")

            elif hours_r == int(hours_r):
                return "{d} {da} and {h} {ho}".format(d = int(days), \
                    da = "days" if int(days) > 1 else "day", h = int(hours_r), \
                        ho = "hours" if int(hours_r) > 1 else "hour")

            else:
                minutes_r = (hours_r - int(hours_r)) * 60
                if minutes_r < 1:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{d} {da}, {h} {ho} and {s} {ss}".format(d = int(days), \
                        da = "days" if int(days) > 1 else "day", h = int(hours_r), \
                            ho = "hours" if int(hours_r) > 1 else "hour", s = round(seconds_r), \
                                ss = "seconds" if round(seconds_r) > 1 else "second")
                elif minutes_r == int(minutes_r):
                    return "{d} {da}, {h} {ho} and {mi} {min}".format(d = int(days), \
                        da = "days" if int(days) > 1 else "day", h = int(hours_r), \
                            ho = "hours" if int(hours_r) > 1 else "hour", mi = int(minutes_r), \
                                min = "minutes" if int(minutes_r) > 1 else "minute")
                else:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{d} {da}, {h} {ho}, {mi} {min} and {s} {ss}".format(d = int(days), \
                        da = "days" if int(days) > 1 else "day", h = int(hours_r), \
                            ho = "hours" if int(hours_r) > 1 else "hour", mi = int(minutes_r), \
                                min = "minutes" if int(minutes_r) > 1 else "minute", s = round(seconds_r), \
                                    ss = "seconds" if round(seconds_r) > 1 else "second")

    elif years == int(years):
        return "{y} {ye}".format(y = int(years), \
            ye = "years" if int(years) > 1 else "year")

    else:
        days_r = (years - int(years)) * 365
        if days_r < 1:
            hours_r = (days_r - int(days_r)) * 24
            if hours_r < 1:
                minutes_r = (hours_r - int(hours_r)) * 60
                if minutes_r < 1:
                    seconds_r = (minutes_r - int(minutes_r)) * 60

                    return "{y} {ye} and {s} {ss}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", s = int(seconds_r), \
                            ss = "seconds" if int(seconds_r) > 1 else "second")

                elif minutes_r == int(minutes_r):
                    return "{y} {ye}, and {mi} {min}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", mi = int(minutes_r), \
                            min = "minutes" if int(minutes_r) > 1 else "minute")

                else:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{y} {ye}, {mi} {min} and {s} {ss}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", mi = int(minutes_r), \
                            min = "minutes" if int(minutes_r) > 1 else "minute", s = int(seconds_r), \
                                ss = "seconds" if int(seconds_r) > 1 else "second")

            elif hours_r == int(hours_r):
                return "{y} {ye} and {h} {ho}".format(y = int(years), \
                    ye = "years" if int(years) > 1 else "year", h = int(hours_r), \
                        ho = "hours" if int(hours_r) > 1 else "hour")

            else:
                minutes_r = (hours_r - int(hours_r)) * 60
                if minutes_r < 1:
                    seconds_r = (minutes_r - int(minutes_r)) * 60

                    return "{y} {ye}, {h} {ho} and {s} {ss}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", h = int(hours_r), \
                            ho = "hours" if int(hours_r) > 1 else "hour", s = int(seconds_r), \
                                ss = "seconds" if int(seconds_r) > 1 else "second")

                elif minutes_r == int({minutes_r}):
                    return "{y} {ye}, {h} {ho} and {mi} {min}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", mi = int(minutes_r), \
                            min = "minutes" if int(minutes_r) > 1 else "minute")

                else:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{y} {ye}, {h} {ho}, {mi} {min} and {s} {ss}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", h = int(hours_r), \
                            ho = "hours" if int(hours_r) > 1 else "hour", mi = int(minutes_r), \
                                min = "minutes" if int(minutes_r) > 1 else "minute", s = int(seconds_r), \
                                    ss = "seconds" if int(seconds_r) > 1 else "second")

        elif days_r == int(days_r):
            return "{y} {ye} and {d} {da}".format(y = int(years), \
                ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                    da = "days" if int(days_r) > 1 else "day")

        else:
            hours_r = (days_r - int(days_r)) * 24
            if hours_r < 1:
                minutes_r = (hours_r - int(hours_r)) * 60
                if minutes_r < 1:
                    seconds_r = (minutes_r - int(minutes_r)) * 60

                    return "{y} {ye}, {d} {da} and {s} {ss}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                            da = "days" if int(days_r) > 1 else "day", s = int(seconds_r), \
                                ss = "seconds" if int(seconds_r) > 1 else "second")

                elif minutes_r == int(minutes_r):
                    return "{y} {ye}, {d} {da} and {mi} {min}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                            da = "days" if int(days_r) > 1 else "day", mi = int(minutes_r), \
                                min = "minutes" if int(minutes_r) > 1 else "minute")

                else:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{y} {ye}, {d} {da}, {mi} {min} and {s} {ss}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                            da = "days" if int(days_r) > 1 else "day", mi = int(minutes_r), \
                                min = "minutes" if int(minutes_r) > 1 else "minute", s = int(seconds_r), \
                                    ss = "seconds" if int(seconds_r) > 1 else "second")

            elif hours_r == int(hours_r):
                return "{y} {ye}, {d} {da} and {h} {ho}".format(y = int(years), \
                    ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                        da = "days" if int(days_r) > 1 else "day", h = int(hours_r), \
                            ho = "hours" if int(hours_r) > 1 else "hour")
            else:
                minutes_r = (hours_r - int(hours_r)) * 60

                if minutes_r < 1:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    return "{y} {ye}, {d} {da}, {h} {ho} and {s} {ss}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                            da = "days" if int(days_r) > 1 else "day", h = int(hours_r), \
                                ho = "hours" if int(hours_r) > 1 else "hour", s = int(seconds_r), \
                                    ss = "seconds" if int(seconds) > 1 else "second")

                elif minutes_r == int(minutes_r):
                    return "{y} {ye}, {d} {da}, {h} {ho} and {mi} {min}".format(y = int(years), \
                        ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                            da = "days" if int(days_r) > 1 else "day", h = int(hours_r), \
                                ho = "hours" if int(hours_r) > 1 else "hour", mi = int(minutes_r), \
                                    min = "minutes" if int(minutes_r) > 1 else "minute")

                else:
                    seconds_r = (minutes_r - int(minutes_r)) * 60
                    if round(seconds_r) < 1:
                        return "{y} {ye}, {d} {da}, {h} {ho} and {mi} {min}".format(y = int(years), \
                            ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                                da = "days" if int(days_r) > 1 else "day", h = int(hours_r), \
                                    ho = "hours" if int(hours_r) > 1 else "hour", mi = int(minutes_r), \
                                        min = "minutes" if int(minutes_r) > 1 else "minute")
                    else:
                        return "{y} {ye}, {d} {da}, {h} {ho}, {mi} {min} and {s} {ss}".format(y = int(years), \
                            ye = "years" if int(years) > 1 else "year", d = int(days_r), \
                                da = "days" if int(days_r) > 1 else "day", h = int(hours_r), \
                                    ho = "hours" if int(hours_r) > 1 else "hour", mi = int(minutes_r), \
                                        min = "minutes" if int(minutes_r) > 1 else "minute", s = round(seconds_r), \
                                            ss = "seconds" if round(seconds_r) > 1 else "second")
