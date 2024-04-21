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