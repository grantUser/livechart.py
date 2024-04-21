import requests


class Livechart:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.url = "https://www.livechart.me/graphql"
        self.headers = {
            "User-Agent": "me.livechart.android/7.5.3 (Linux; Android 11 SDK 30; Google sdk_gphone_x86)"
        }

    def graphql(self, operationName, variables, query):
        payload = {
            "operationName": operationName,
            "variables": variables,
            "query": query,
        }
        response = self.session.post(
            self.url, headers=self.headers, json=payload
        ).json()
        if "data" in response:
            return response["data"]
        else:
            return None

    def Timetable(
        self, date, timeZone, dayCount, titlePreference, markFilters, viewingPreferences
    ):
        """
        Retrieve the timetable for anime releases based on the specified parameters.

        Args:
            date (str): The date for which the timetable is requested. Should be in the format 'YYYY-MM-DD'.
            timeZone (str): The time zone in which the timetable should be returned.
            dayCount (int): The number of days for which the timetable should be retrieved, starting from the specified date.
            titlePreference (str): The language preference for the titles of the anime. Possible values: 'ROMAJI', 'ENGLISH', 'NATIVE'.
            markFilters (dict): Filters to apply to the release marks. Should be a dictionary containing:
                - 'excludeStatuses' (list of str): Statuses to exclude from the timetable. Possible values: 'PAUSED', 'DROPPED', 'SKIPPING'.
                - 'excludeUnmarked' (bool): Whether to exclude unmarked releases. True to exclude, False to include.
            viewingPreferences (dict): Preferences for the viewer. Should be a dictionary containing:
                - 'preferredLanguages' (list of str): Preferred languages for viewing. Leave empty for default.
        """

        operationName = "Timetable"
        variables = {
            "date": date,
            "timeZone": timeZone,
            "dayCount": dayCount,
            "titlePreference": titlePreference,
            "markFilters": markFilters,
            "viewingPreferences": viewingPreferences,
        }
        query = "query Timetable($date: ISO8601Date, $timeZone: TimeZoneName, $dayCount: Int, $titlePreference: TitleLanguage, $markFilters: MarkFiltersInput, $viewingPreferences: ViewingPreferencesInput) { timetable(date: $date, timeZone: $timeZone, dayCount: $dayCount, titlePreference: $titlePreference, markFilters: $markFilters, viewingPreferences: $viewingPreferences) { __typename ...releaseListingsFields days { __typename ...releaseDayFields timeslots { time approximate notes { __typename ...schedulingNoteAndRelationsFragment } releases { __typename ...animeReleaseAndRelationsFragment } } } } }  fragment releaseListingsFields on ReleaseListings { nextDay prevDay nextWeek prevWeek timeZone }  fragment releaseDayFields on ReleaseDay { date beginningOfDay endOfDay }  fragment schedulingNoteFields on SchedulingNote { databaseId releaseScheduleDatabaseId createdAt updatedAt sentiment gist message { markdown } releaseDate timeIsApproximate animeDatabaseId action { url labelText } }  fragment dateTimeWithPrecisionFields on DateTimeWithPrecision { dateTime: value dateTimePrecision: precision }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment animeSnippetFields on Anime { id databaseId romajiTitle englishTitle nativeTitle alternativeTitles format formatLabel category sourceMaterialDatabaseId updatedAt createdAt releaseStatus premiereSeason { yearQuarter } startDate { __typename ...dateTimeWithPrecisionFields } aggregateRating { count weightedValue bestPossible worstPossible } episodeInfo { count duration } editorNote { markdown } poster { __typename ...onTheFlyImageFields } }  fragment releaseNetworkFields on AnimeReleaseNetwork { databaseId name shortName accentColorOnLight { hex } accentColorOnDark { hex } updatedAt }  fragment episodeNumberRangeFields on EpisodeNumberRange { minNumber minReleaseNumber size label lastOfAnime lastOfSchedule }  fragment episodeRangeFields on EpisodeRange { numberRange { __typename ...episodeNumberRangeFields } date timeIsApproximate }  fragment releaseSeasonFragment on ReleaseSeason { title slug yearQuarter startDate endDate }  fragment dateWithPrecisionFields on DateWithPrecision { date: value datePrecision: precision }  fragment episodeRangePlaceholderFields on EpisodeRangePlaceholder { numberRange { __typename ...episodeNumberRangeFields } value { __typename ... on ApproximateReleaseMessage { body } ... on ReleaseSeason { __typename ...releaseSeasonFragment } ... on DateWithPrecision { __typename ...dateWithPrecisionFields } ... on DateTimeWithPrecision { __typename ...dateTimeWithPrecisionFields } } }  fragment releaseScheduleStateFields on ReleaseScheduleState { databaseId animeDatabaseId releaseScheduleDatabaseId schedulingNoteDatabaseId networkName networkShortName scheduleTitle scheduleShortTitle includeNetworkInShortTitle releaseStatus updatedAt previousRelease { __typename ...episodeRangeFields } nextRelease { __typename ...episodeRangeFields } nextReleasePlaceholder { __typename ...episodeRangePlaceholderFields } accentColorOnLight { hex } accentColorOnDark { hex } action { url labelText iconMaskUrl } }  fragment releaseScheduleFields on AnimeReleaseSchedule { databaseId animeDatabaseId networkDatabaseId title shortTitle includeNetworkInShortTitle applicableToViewer pinned pinnedByViewer defaultForViewer viewerNotificationsPreference updatedAt createdAt network { __typename ...releaseNetworkFields } releaseState { __typename ...releaseScheduleStateFields } }  fragment releaseScheduleAndNetworkFragment on AnimeReleaseSchedule { __typename ...releaseScheduleFields network { __typename ...releaseNetworkFields } }  fragment schedulingNoteAndRelationsFragment on SchedulingNote { __typename ...schedulingNoteFields anime { __typename ...animeSnippetFields } releaseSchedule { __typename ...releaseScheduleAndNetworkFragment } }  fragment animeReleaseFields on AnimeRelease { id animeDatabaseId releaseScheduleDatabaseId episodeRanges { __typename ...episodeRangeFields } updatedAt }  fragment viewerLibraryEntryFields on ViewerLibraryEntry { animeDatabaseId episodesWatched rewatches status rating ratingScale notes startedAt finishedAt updatedAt createdAt }  fragment animeSnippetAndLibraryEntryFragment on Anime { __typename ...animeSnippetFields viewerLibraryEntry { __typename ...viewerLibraryEntryFields } }  fragment animeReleaseAndRelationsFragment on AnimeRelease { __typename ...animeReleaseFields releaseSchedule { __typename ...releaseScheduleFields network { __typename ...releaseNetworkFields } } anime { __typename ...animeSnippetAndLibraryEntryFragment } }"

        return self.graphql(operationName, variables, query)

    def GetFullSingleAnime(self, id, viewingPreferences):
        """
        Retrieve detailed information about a single anime based on its ID.

        Args:
            id (str): The ID of the anime.
            viewingPreferences (dict): Preferences for the viewer. Should be a dictionary containing:
                - 'preferredLanguages' (list of str): Preferred languages for viewing. Leave empty for default.
        """

        operationName = "GetFullSingleAnime"
        variables = {"id": id, "viewingPreferences": viewingPreferences}
        query = "query GetFullSingleAnime($id: ID!, $viewingPreferences: ViewingPreferencesInput) { singleAnime(id: $id) { __typename ...fullAnimeFragment } }  fragment dateTimeWithPrecisionFields on DateTimeWithPrecision { dateTime: value dateTimePrecision: precision }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment animeSnippetFields on Anime { id databaseId romajiTitle englishTitle nativeTitle alternativeTitles format formatLabel category sourceMaterialDatabaseId updatedAt createdAt releaseStatus premiereSeason { yearQuarter } startDate { __typename ...dateTimeWithPrecisionFields } aggregateRating { count weightedValue bestPossible worstPossible } episodeInfo { count duration } editorNote { markdown } poster { __typename ...onTheFlyImageFields } }  fragment twitterFragment on TwitterProfile { username url }  fragment animeDetailsFields on Anime { databaseId updatedAt createdAt hasStreams hasVideos websiteUrl malUrl anidbUrl anilistUrl kitsuUrl animePlanetUrl anisearchUrl annUrl franchiseMembership { defaultFranchiseDatabaseId franchiseCount } synopsis { markdown emended spoilerNote containsSpoilers source sourceUrl } twitterProfile { __typename ...twitterFragment } }  fragment episodeNumberRangeFields on EpisodeNumberRange { minNumber minReleaseNumber size label lastOfAnime lastOfSchedule }  fragment episodeRangeFields on EpisodeRange { numberRange { __typename ...episodeNumberRangeFields } date timeIsApproximate }  fragment releaseSeasonFragment on ReleaseSeason { title slug yearQuarter startDate endDate }  fragment dateWithPrecisionFields on DateWithPrecision { date: value datePrecision: precision }  fragment episodeRangePlaceholderFields on EpisodeRangePlaceholder { numberRange { __typename ...episodeNumberRangeFields } value { __typename ... on ApproximateReleaseMessage { body } ... on ReleaseSeason { __typename ...releaseSeasonFragment } ... on DateWithPrecision { __typename ...dateWithPrecisionFields } ... on DateTimeWithPrecision { __typename ...dateTimeWithPrecisionFields } } }  fragment releaseScheduleStateFields on ReleaseScheduleState { databaseId animeDatabaseId releaseScheduleDatabaseId schedulingNoteDatabaseId networkName networkShortName scheduleTitle scheduleShortTitle includeNetworkInShortTitle releaseStatus updatedAt previousRelease { __typename ...episodeRangeFields } nextRelease { __typename ...episodeRangeFields } nextReleasePlaceholder { __typename ...episodeRangePlaceholderFields } accentColorOnLight { hex } accentColorOnDark { hex } action { url labelText iconMaskUrl } }  fragment schedulingNoteFields on SchedulingNote { databaseId releaseScheduleDatabaseId createdAt updatedAt sentiment gist message { markdown } releaseDate timeIsApproximate animeDatabaseId action { url labelText } }  fragment viewerLibraryEntryFields on ViewerLibraryEntry { animeDatabaseId episodesWatched rewatches status rating ratingScale notes startedAt finishedAt updatedAt createdAt }  fragment sourceMaterialFields on SourceMaterial { databaseId name tagDatabaseId createdAt updatedAt }  fragment tagFields on Tag { databaseId name classification classificationLabel ageRestricted createdAt updatedAt }  fragment favoritableFields on Favoritable { id favoriteCount viewerHasFavorited }  fragment studioFields on Studio { __typename id databaseId name nativeName websiteUrl facebookUrl createdAt updatedAt ...favoritableFields twitterProfile { __typename ...twitterFragment } defunctDate { __typename ...dateWithPrecisionFields } foundedDate { __typename ...dateWithPrecisionFields } logo { __typename ...onTheFlyImageFields } }  fragment franchiseInstallmentFields on FranchiseInstallment { databaseId franchiseDatabaseId animeDatabaseId label description { markdown } updatedAt createdAt }  fragment franchiseFields on Franchise { databaseId slug englishName romajiName defaultOrderDatabaseId description { markdown } updatedAt createdAt }  fragment franchiseInstallmentAndFranchiseFragment on FranchiseInstallment { __typename ...franchiseInstallmentFields franchise { __typename ...franchiseFields } }  fragment fullAnimeFragment on Anime { __typename ...animeSnippetFields ...animeDetailsFields releaseState(viewingPreferences: $viewingPreferences) { __typename ...releaseScheduleStateFields schedulingNote { __typename ...schedulingNoteFields } } viewerLibraryEntry { __typename ...viewerLibraryEntryFields } sourceMaterial { __typename ...sourceMaterialFields } tags { __typename ...tagFields } studios { __typename ...studioFields } franchiseInstallments { __typename ...franchiseInstallmentAndFranchiseFragment } }"

        return self.graphql(operationName, variables, query)

    def GetFranchiseInstallments(self, franchiseId, titlePreference, first, last):
        """
        Retrieve franchise installments based on the specified parameters.

        Args:
            franchiseId (str): The ID of the franchise.
            titlePreference (str): The language preference for the titles of the installments. Possible values: 'ROMAJI', 'ENGLISH', 'NATIVE'.
            first (int): The number of installments to retrieve from the beginning of the list.
            last (int): The number of installments to retrieve from the end of the list.
        """

        operationName = "GetFranchiseInstallments"
        variables = {
            "franchiseId": franchiseId,
            "titlePreference": titlePreference,
            "first": first,
            "last": last,
        }
        query = "query GetFranchiseInstallments($franchiseId: ID!, $orderId: ID, $titlePreference: TitleLanguage, $beforeCursor: String, $afterCursor: String, $first: Int, $last: Int) { franchise(id: $franchiseId) { __typename ...franchiseFields installments(orderId: $orderId, titlePreference: $titlePreference, before: $beforeCursor, after: $afterCursor, first: $first, last: $last) { nodes { __typename ...franchiseInstallmentAndAnimeFragment } pageInfo { __typename ...pageInfoFragment } } } }  fragment franchiseFields on Franchise { databaseId slug englishName romajiName defaultOrderDatabaseId description { markdown } updatedAt createdAt }  fragment franchiseInstallmentFields on FranchiseInstallment { databaseId franchiseDatabaseId animeDatabaseId label description { markdown } updatedAt createdAt }  fragment dateTimeWithPrecisionFields on DateTimeWithPrecision { dateTime: value dateTimePrecision: precision }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment animeSnippetFields on Anime { id databaseId romajiTitle englishTitle nativeTitle alternativeTitles format formatLabel category sourceMaterialDatabaseId updatedAt createdAt releaseStatus premiereSeason { yearQuarter } startDate { __typename ...dateTimeWithPrecisionFields } aggregateRating { count weightedValue bestPossible worstPossible } episodeInfo { count duration } editorNote { markdown } poster { __typename ...onTheFlyImageFields } }  fragment viewerLibraryEntryFields on ViewerLibraryEntry { animeDatabaseId episodesWatched rewatches status rating ratingScale notes startedAt finishedAt updatedAt createdAt }  fragment franchiseInstallmentAndAnimeFragment on FranchiseInstallment { __typename ...franchiseInstallmentFields anime { __typename ...animeSnippetFields viewerLibraryEntry { __typename ...viewerLibraryEntryFields } } }  fragment pageInfoFragment on PageInfo { hasPreviousPage hasNextPage startCursor endCursor }"

        return self.graphql(operationName, variables, query)

    def GetAnimeVideosByAnime(self, first, last, availableInViewerRegion, animeId):
        """
        Retrieve anime videos based on the specified parameters.

        Args:
            first (int): The number of videos to retrieve from the beginning of the list.
            last (int): The number of videos to retrieve from the end of the list.
            availableInViewerRegion (bool): Whether the videos should be available in the viewer's region.
            animeId (str): The ID of the anime.
        """

        operationName = "GetAnimeVideosByAnime"
        variables = {
            "first": first,
            "last": last,
            "availableInViewerRegion": availableInViewerRegion,
            "animeId": animeId,
        }
        query = "query GetAnimeVideosByAnime($beforeCursor: String, $afterCursor: String, $first: Int, $last: Int, $availableInViewerRegion: Boolean, $animeId: ID!) { animeVideos(before: $beforeCursor, after: $afterCursor, first: $first, last: $last, availableInViewerRegion: $availableInViewerRegion, animeId: $animeId) { nodes { __typename ...fullAnimeVideoFragment } pageInfo { __typename ...pageInfoFragment } } }  fragment animeVideoFields on AnimeVideo { databaseId videoDatabaseId animeDatabaseId url embedUrl title duration containsSpoilers spoilerNote position updatedAt createdAt }  fragment videoFields on Video { databaseId title duration aspectRatio thumbnailUrl url embedUrl embeddable availableInViewerRegion liveStartTime liveEndTime uploadedAt updatedAt createdAt }  fragment mediaTrackFields on MediaTrack { languageCode shortLabel category }  fragment languageFields on Language { code name nativeName shortName }  fragment fullMediaTrackFragment on MediaTrack { __typename ...mediaTrackFields language { __typename ...languageFields } }  fragment fullVideoFragment on Video { __typename ...videoFields tracks { __typename ...fullMediaTrackFragment } }  fragment fullAnimeVideoFragment on AnimeVideo { __typename ...animeVideoFields video { __typename ...fullVideoFragment } }  fragment pageInfoFragment on PageInfo { hasPreviousPage hasNextPage startCursor endCursor }"

        return self.graphql(operationName, variables, query)

    def GetLegacyStreams(self, first, last, availableInViewerRegion, animeId):
        """
        Retrieve legacy streams based on the specified parameters.

        Args:
            first (int): The number of streams to retrieve from the beginning of the list.
            last (int): The number of streams to retrieve from the end of the list.
            availableInViewerRegion (bool): Whether the streams should be available in the viewer's region.
            animeId (str): The ID of the anime.
        """

        operationName = "GetLegacyStreams"
        variables = {
            "first": first,
            "last": last,
            "availableInViewerRegion": availableInViewerRegion,
            "animeId": animeId,
        }
        query = "query GetLegacyStreams($beforeCursor: String, $afterCursor: String, $first: Int, $last: Int, $availableInViewerRegion: Boolean, $animeId: ID!) { legacyStreams(before: $beforeCursor, after: $afterCursor, first: $first, last: $last, availableInViewerRegion: $availableInViewerRegion, animeId: $animeId) { nodes { __typename ...legacyStreamFragment } pageInfo { __typename ...pageInfoFragment } } }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment legacyStreamFragment on LegacyStream { databaseId animeDatabaseId streamingServiceDatabaseId url comment availableInViewerRegion displayName updatedAt createdAt streamingService { databaseId name logo { __typename ...onTheFlyImageFields } updatedAt createdAt } }  fragment pageInfoFragment on PageInfo { hasPreviousPage hasNextPage startCursor endCursor }"

        return self.graphql(operationName, variables, query)

    def GetAnimeReleaseSchedules(self, animeId, viewingPreferences, first, last):
        """
        Retrieve anime release schedules based on the specified parameters.

        Args:
            animeId (str): The ID of the anime.
            viewingPreferences (dict): Preferences for the viewer. Should be a dictionary containing:
                - 'preferredLanguages' (list of str): Preferred languages for viewing.
            first (int): The number of release schedules to retrieve from the beginning of the list.
            last (int): The number of release schedules to retrieve from the end of the list.
        """

        operationName = "GetAnimeReleaseSchedules"
        variables = {
            "animeId": animeId,
            "viewingPreferences": viewingPreferences,
            "first": first,
            "last": last,
        }
        query = "query GetAnimeReleaseSchedules($animeId: ID!, $viewingPreferences: ViewingPreferencesInput, $beforeCursor: String, $afterCursor: String, $first: Int, $last: Int) { singleAnime(id: $animeId) { originalLanguageCodes releaseSchedules(viewingPreferences: $viewingPreferences, before: $beforeCursor, after: $afterCursor, first: $first, last: $last) { nodes { __typename ...releaseScheduleAndRelationsFragment } pageInfo { __typename ...pageInfoFragment } } } }  fragment releaseNetworkFields on AnimeReleaseNetwork { databaseId name shortName accentColorOnLight { hex } accentColorOnDark { hex } updatedAt }  fragment episodeNumberRangeFields on EpisodeNumberRange { minNumber minReleaseNumber size label lastOfAnime lastOfSchedule }  fragment episodeRangeFields on EpisodeRange { numberRange { __typename ...episodeNumberRangeFields } date timeIsApproximate }  fragment releaseSeasonFragment on ReleaseSeason { title slug yearQuarter startDate endDate }  fragment dateWithPrecisionFields on DateWithPrecision { date: value datePrecision: precision }  fragment dateTimeWithPrecisionFields on DateTimeWithPrecision { dateTime: value dateTimePrecision: precision }  fragment episodeRangePlaceholderFields on EpisodeRangePlaceholder { numberRange { __typename ...episodeNumberRangeFields } value { __typename ... on ApproximateReleaseMessage { body } ... on ReleaseSeason { __typename ...releaseSeasonFragment } ... on DateWithPrecision { __typename ...dateWithPrecisionFields } ... on DateTimeWithPrecision { __typename ...dateTimeWithPrecisionFields } } }  fragment releaseScheduleStateFields on ReleaseScheduleState { databaseId animeDatabaseId releaseScheduleDatabaseId schedulingNoteDatabaseId networkName networkShortName scheduleTitle scheduleShortTitle includeNetworkInShortTitle releaseStatus updatedAt previousRelease { __typename ...episodeRangeFields } nextRelease { __typename ...episodeRangeFields } nextReleasePlaceholder { __typename ...episodeRangePlaceholderFields } accentColorOnLight { hex } accentColorOnDark { hex } action { url labelText iconMaskUrl } }  fragment releaseScheduleFields on AnimeReleaseSchedule { databaseId animeDatabaseId networkDatabaseId title shortTitle includeNetworkInShortTitle applicableToViewer pinned pinnedByViewer defaultForViewer viewerNotificationsPreference updatedAt createdAt network { __typename ...releaseNetworkFields } releaseState { __typename ...releaseScheduleStateFields } }  fragment releaseScheduleAndNetworkFragment on AnimeReleaseSchedule { __typename ...releaseScheduleFields network { __typename ...releaseNetworkFields } }  fragment releaseScheduleDetailsFields on AnimeReleaseSchedule { databaseId updatedAt description { markdown } startDate { __typename ...dateTimeWithPrecisionFields } endDate { __typename ...dateTimeWithPrecisionFields } }  fragment schedulingNoteFields on SchedulingNote { databaseId releaseScheduleDatabaseId createdAt updatedAt sentiment gist message { markdown } releaseDate timeIsApproximate animeDatabaseId action { url labelText } }  fragment mediaTrackFields on MediaTrack { languageCode shortLabel category }  fragment languageFields on Language { code name nativeName shortName }  fragment fullMediaTrackFragment on MediaTrack { __typename ...mediaTrackFields language { __typename ...languageFields } }  fragment releaseScheduleAndRelationsFragment on AnimeReleaseSchedule { __typename ...releaseScheduleAndNetworkFragment ...releaseScheduleDetailsFields releaseState { __typename ...releaseScheduleStateFields schedulingNote { __typename ...schedulingNoteFields } } tracks { __typename ...fullMediaTrackFragment } }  fragment pageInfoFragment on PageInfo { hasPreviousPage hasNextPage startCursor endCursor }"

        return self.graphql(operationName, variables, query)

    def GetAnimeVisuals(self, animeId, preferredLanguages, first, last):
        """
        Retrieve visuals for a specific anime based on the specified parameters.

        Args:
            animeId (str): The ID of the anime.
            preferredLanguages (list of str): Preferred languages for visuals.
            first (int): The number of visuals to retrieve from the beginning of the list.
            last (int): The number of visuals to retrieve from the end of the list.
        """

        operationName = "GetAnimeVisuals"
        variables = {
            "animeId": animeId,
            "preferredLanguages": preferredLanguages,
            "first": first,
            "last": last,
        }
        query = "query GetAnimeVisuals($animeId: ID!, $preferredLanguages: [String!], $beforeCursor: String, $afterCursor: String, $first: Int, $last: Int) { singleAnime(id: $animeId) { visuals(preferredLanguages: $preferredLanguages, before: $beforeCursor, after: $afterCursor, first: $first, last: $last) { nodes { __typename ...animeVisualFields } pageInfo { __typename ...pageInfoFragment } } } }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment animeVisualFields on AnimeVisual { databaseId animeDatabaseId position updatedAt createdAt label description { markdown } spoilerNote containsSpoilers copyrightNotice shortCopyrightNotice dimensions { aspectRatio orientation } image { __typename ...onTheFlyImageFields } }  fragment pageInfoFragment on PageInfo { hasPreviousPage hasNextPage startCursor endCursor }"

        return self.graphql(operationName, variables, query)

    def GetHeadlines(self, first, last, relatedTo):
        """
        Retrieve headlines based on the specified parameters.

        Args:
            first (int): The number of headlines to retrieve from the beginning of the list.
            last (int): The number of headlines to retrieve from the end of the list.
            relatedTo (str): The ID of the related item.
        """

        operationName = "GetHeadlines"
        variables = {"first": first, "last": last, "relatedTo": relatedTo}
        query = "query GetHeadlines($beforeCursor: String, $afterCursor: String, $first: Int, $last: Int, $relatedTo: ID) { headlines(before: $beforeCursor, after: $afterCursor, first: $first, last: $last, relatedTo: $relatedTo) { nodes { __typename ...headlineFields } pageInfo { __typename ...pageInfoFragment } } }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment headlineRelatablesCollectionMetaDataFields on HeadlineRelatablesCollection { totalCount }  fragment headlineFields on Headline { databaseId title subTitle sponsored targetUrl targetHost createdAt updatedAt edited thumbnail { __typename ...onTheFlyImageFields } relatedAnime { __typename ...headlineRelatablesCollectionMetaDataFields } relatedStudios { __typename ...headlineRelatablesCollectionMetaDataFields } }  fragment pageInfoFragment on PageInfo { hasPreviousPage hasNextPage startCursor endCursor }"

        return self.graphql(operationName, variables, query)

    def ChartPlacements(
        self,
        chartId,
        sort,
        category,
        titlePreference,
        markFilters,
        ongoingFilter,
        viewingPreferences,
        first,
        last,
    ):
        """
        Retrieve chart placements based on the specified parameters.

        Args:
            chartId (str): The ID of the chart.
            sort (dict): Sorting options. Should be a dictionary containing:
                - 'algorithm' (str): The sorting algorithm (e.g., "POPULARITY", "NEXT_EPISODE_COUNTDOWN", "AVERAGE_RATING", "DATE", "ANIME_UPDATED_AT", "ANIME_TITLE").
                - 'direction' (str): The sorting direction (e.g., "DESC" for descending, "ASC" for ascending).
            category (str): The category of anime placements ("TV", "MOVIES", "OVAS", or null for all categories).
            titlePreference (str): The language preference for the titles of the anime.
            markFilters (dict): Filters to apply to the release marks. Should be a dictionary containing:
                - 'excludeStatuses' (list of str): Statuses to exclude from the timetable. Possible values: 'PAUSED', 'DROPPED', 'SKIPPING'.
                - 'excludeUnmarked' (bool): Whether to exclude unmarked releases. True to exclude, False to include.
            ongoingFilter (str): Filter for ongoing anime.
            viewingPreferences (dict): Preferences for the viewer. Should be a dictionary containing:
                - 'preferredLanguages' (list of str): Preferred languages for viewing. Leave empty for default.
            first (int): The number of placements to retrieve from the beginning of the list.
            last (int): The number of placements to retrieve from the end of the list.
        """

        operationName = "ChartPlacements"
        variables = {
            "chartId": chartId,
            "sort": sort,
            "category": category,
            "titlePreference": titlePreference,
            "markFilters": markFilters,
            "ongoingFilter": ongoingFilter,
            "viewingPreferences": viewingPreferences,
            "first": first,
            "last": last,
        }
        query = "query ChartPlacements($chartId: ID, $sort: AnimeChartPlacementSort!, $category: AnimeCategory, $titlePreference: TitleLanguage, $markFilters: MarkFiltersInput, $ongoingFilter: OngoingFilter, $beforeCursor: String, $afterCursor: String, $viewingPreferences: ViewingPreferencesInput, $first: Int, $last: Int) { chart(id: $chartId) { animePlacements(category: $category, sort: $sort, titlePreference: $titlePreference, markFilters: $markFilters, ongoingFilter: $ongoingFilter, before: $beforeCursor, after: $afterCursor, first: $first, last: $last) { nodes { __typename ...animeChartPlacementFields anime { __typename ...animeSnippetFields viewerLibraryEntry { __typename ...viewerLibraryEntryFields } releaseState(viewingPreferences: $viewingPreferences) { __typename ...releaseScheduleStateFields } } } pageInfo { __typename ...pageInfoFragment } } } }  fragment dateTimeWithPrecisionFields on DateTimeWithPrecision { dateTime: value dateTimePrecision: precision }  fragment animeChartPlacementFields on AnimeChartPlacement { databaseId chartDatabaseId animeDatabaseId yearQuarter editorNote leftover ongoingOffset date { __typename ...dateTimeWithPrecisionFields } updatedAt createdAt }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment animeSnippetFields on Anime { id databaseId romajiTitle englishTitle nativeTitle alternativeTitles format formatLabel category sourceMaterialDatabaseId updatedAt createdAt releaseStatus premiereSeason { yearQuarter } startDate { __typename ...dateTimeWithPrecisionFields } aggregateRating { count weightedValue bestPossible worstPossible } episodeInfo { count duration } editorNote { markdown } poster { __typename ...onTheFlyImageFields } }  fragment viewerLibraryEntryFields on ViewerLibraryEntry { animeDatabaseId episodesWatched rewatches status rating ratingScale notes startedAt finishedAt updatedAt createdAt }  fragment episodeNumberRangeFields on EpisodeNumberRange { minNumber minReleaseNumber size label lastOfAnime lastOfSchedule }  fragment episodeRangeFields on EpisodeRange { numberRange { __typename ...episodeNumberRangeFields } date timeIsApproximate }  fragment releaseSeasonFragment on ReleaseSeason { title slug yearQuarter startDate endDate }  fragment dateWithPrecisionFields on DateWithPrecision { date: value datePrecision: precision }  fragment episodeRangePlaceholderFields on EpisodeRangePlaceholder { numberRange { __typename ...episodeNumberRangeFields } value { __typename ... on ApproximateReleaseMessage { body } ... on ReleaseSeason { __typename ...releaseSeasonFragment } ... on DateWithPrecision { __typename ...dateWithPrecisionFields } ... on DateTimeWithPrecision { __typename ...dateTimeWithPrecisionFields } } }  fragment releaseScheduleStateFields on ReleaseScheduleState { databaseId animeDatabaseId releaseScheduleDatabaseId schedulingNoteDatabaseId networkName networkShortName scheduleTitle scheduleShortTitle includeNetworkInShortTitle releaseStatus updatedAt previousRelease { __typename ...episodeRangeFields } nextRelease { __typename ...episodeRangeFields } nextReleasePlaceholder { __typename ...episodeRangePlaceholderFields } accentColorOnLight { hex } accentColorOnDark { hex } action { url labelText iconMaskUrl } }  fragment pageInfoFragment on PageInfo { hasPreviousPage hasNextPage startCursor endCursor }"

        return self.graphql(operationName, variables, query)

    def GetChart(self, id, default, nearestOfSeason):
        """
        Retrieve chart details based on the specified parameters.

        Args:
            id (str, optional): The ID of the chart. Defaults to None.
            default (str): Default chart mode. Possible values: "CURRENT", "NEAREST". Defaults to "CURRENT".
            nearestOfSeason (str, optional): Season nearest to the specified one. Defaults to None.
        """

        operationName = "GetChart"
        variables = {"id": id, "default": default, "nearestOfSeason": nearestOfSeason}
        query = "query GetChart($id: ID, $default: DefaultChartMode, $nearestOfSeason: Season) { chart(id: $id, default: $default, nearestOfSeason: $nearestOfSeason) { __typename ...chartFields ...chartRelativeSeasonFields } }  fragment chartFields on Chart { databaseId season { yearQuarter slug } updatedAt createdAt }  fragment chartRelativeSeasonFields on DeepChart { previousSeason { yearQuarter } nextSeason { yearQuarter } }"

        return self.graphql(operationName, variables, query)
    

    def GetStudio(self, id):
        """
        Retrieve information about a studio based on the provided ID.

        Args:
            id (str): The ID of the studio.
        """

        operationName = "GetStudio"
        variables = {"id": id}
        query = "query GetStudio($id: ID!) { studio(id: $id) { __typename ...studioFields } }  fragment favoritableFields on Favoritable { id favoriteCount viewerHasFavorited }  fragment twitterFragment on TwitterProfile { username url }  fragment dateWithPrecisionFields on DateWithPrecision { date: value datePrecision: precision }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment studioFields on Studio { __typename id databaseId name nativeName websiteUrl facebookUrl createdAt updatedAt ...favoritableFields twitterProfile { __typename ...twitterFragment } defunctDate { __typename ...dateWithPrecisionFields } foundedDate { __typename ...dateWithPrecisionFields } logo { __typename ...onTheFlyImageFields } }"
        return self.graphql(operationName, variables, query)


    def StudioAnime(self, id, beforeCursor, afterCursor, first, last, viewingPreferences, sort, titlePreference):
        """
        Retrieve information about anime produced by a studio based on the provided studio ID.

        Args:
            id (str): The ID of the studio.
            beforeCursor (str, optional): A cursor that points to the item before the current page of results.
            afterCursor (str, optional): A cursor that points to the item after the current page of results.
            first (int, optional): Maximum number of items to retrieve from the previous page.
            last (int, optional): Maximum number of items to retrieve from the next page.
        """

        operationName = "StudioAnime"
        variables = {
            "id": id,
            "beforeCursor": beforeCursor,
            "afterCursor": afterCursor,
            "first": first,
            "last": last,
            "viewingPreferences": viewingPreferences,
            "sort": sort,
            "titlePreference": titlePreference
        }
        query = "query StudioAnime($id: ID!, $beforeCursor: String, $afterCursor: String, $first: Int, $last: Int, $viewingPreferences: ViewingPreferencesInput, $sort: AnimeSort, $titlePreference: TitleLanguage) { studio(id: $id) { anime(before: $beforeCursor, after: $afterCursor, first: $first, last: $last, sort: $sort, titlePreference: $titlePreference) { __typename ...animeConnectionFragment } } }  fragment dateTimeWithPrecisionFields on DateTimeWithPrecision { dateTime: value dateTimePrecision: precision }  fragment onTheFlyImageFields on OnTheFlyImage { urlTemplate cacheNamespace styles { name formats width height } }  fragment animeSnippetFields on Anime { id databaseId romajiTitle englishTitle nativeTitle alternativeTitles format formatLabel category sourceMaterialDatabaseId updatedAt createdAt releaseStatus premiereSeason { yearQuarter } startDate { __typename ...dateTimeWithPrecisionFields } aggregateRating { count weightedValue bestPossible worstPossible } episodeInfo { count duration } editorNote { markdown } poster { __typename ...onTheFlyImageFields } }  fragment episodeNumberRangeFields on EpisodeNumberRange { minNumber minReleaseNumber size label lastOfAnime lastOfSchedule }  fragment episodeRangeFields on EpisodeRange { numberRange { __typename ...episodeNumberRangeFields } date timeIsApproximate }  fragment releaseSeasonFragment on ReleaseSeason { title slug yearQuarter startDate endDate }  fragment dateWithPrecisionFields on DateWithPrecision { date: value datePrecision: precision }  fragment episodeRangePlaceholderFields on EpisodeRangePlaceholder { numberRange { __typename ...episodeNumberRangeFields } value { __typename ... on ApproximateReleaseMessage { body } ... on ReleaseSeason { __typename ...releaseSeasonFragment } ... on DateWithPrecision { __typename ...dateWithPrecisionFields } ... on DateTimeWithPrecision { __typename ...dateTimeWithPrecisionFields } } }  fragment releaseScheduleStateFields on ReleaseScheduleState { databaseId animeDatabaseId releaseScheduleDatabaseId schedulingNoteDatabaseId networkName networkShortName scheduleTitle scheduleShortTitle includeNetworkInShortTitle releaseStatus updatedAt previousRelease { __typename ...episodeRangeFields } nextRelease { __typename ...episodeRangeFields } nextReleasePlaceholder { __typename ...episodeRangePlaceholderFields } accentColorOnLight { hex } accentColorOnDark { hex } action { url labelText iconMaskUrl } }  fragment viewerLibraryEntryFields on ViewerLibraryEntry { animeDatabaseId episodesWatched rewatches status rating ratingScale notes startedAt finishedAt updatedAt createdAt }  fragment animeFragment on Anime { __typename ...animeSnippetFields releaseState(viewingPreferences: $viewingPreferences) { __typename ...releaseScheduleStateFields } viewerLibraryEntry { __typename ...viewerLibraryEntryFields } }  fragment pageInfoFragment on PageInfo { hasPreviousPage hasNextPage startCursor endCursor }  fragment animeConnectionFragment on AnimeConnection { nodes { __typename ...animeFragment } pageInfo { __typename ...pageInfoFragment } }"
        return self.graphql(operationName, variables, query)
