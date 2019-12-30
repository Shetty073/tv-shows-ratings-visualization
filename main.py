from imdb import DATA
from imdb import seasonal_fetch
from plot import plot


def start():
    seasonal_fetch('tt0944947', start=1, end=8)
    x_seasons = []
    seasonal_mean_ratings = []

    mean_rating = 0.00
    for i in DATA:
        x_seasons.append(i)
        ep_count = 0
        total_rating = 0.00
        x_episodes = []
        episode_ratings = []
        for j in DATA[i]:
            # plot episode-wise
            x_episodes.append(j['name'])
            episode_ratings.append(j['rating'])

            # process data for season wise
            total_rating += float(j['rating'])
            ep_count += 1
        mean_rating = total_rating / ep_count
        seasonal_mean_ratings.append(round(mean_rating, 2))

        # plot episode-wise data
        plot(p_type='stem', x_axis=x_episodes, points=[float(x) for x in episode_ratings],
             title=f'GOT - {i.lower()} IMDB episode-wise rating',
             x_label='Episode name', y_label='Rating per episode', y_min_lim=3, y_max_lim=10)

    # plot season-wise
    plot(p_type='plot', x_axis=x_seasons, points=[float(x) for x in seasonal_mean_ratings],
         title='GOT - IMDB season-wise ratings (mean)',
         x_label='Season', y_label='Rating per season (mean)', y_min_lim=3, y_max_lim=10)


# TODO: Implement textual menu
start()
