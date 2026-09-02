---
title: Mobile development and cross-platform — what makes mobile different (app lifecycle and process death, limited memory/battery/network, permissions and sandboxing, app-store distribution and review, device fragmentation, touch and small screens), the declarative UI convergence (SwiftUI and Jetpack Compose: views as functions of state, @State/@Binding/@Observable and remember/State hoisting, recomposition), app architecture (MVVM, unidirectional data flow, UI/domain/data layers, repositories), persistence (SwiftData/Core Data, Room, DataStore/UserDefaults), networking and concurrency (Swift async/await and actors, Kotlin coroutines and Flow), offline-first and sync (local database as source of truth, conflict handling), background work, push notifications, cross-platform choices (React Native, Flutter, Kotlin Multiplatform, PWAs) and their trade-offs, and testing/release
type: concept
section: "7.6"
level: 300
tags: [mobile, ios, android, swift, swiftui, kotlin, jetpack-compose, app-lifecycle, process-death, state-restoration, background, foreground, memory-pressure, battery, permissions, sandbox, app-store, play-store, review, fragmentation, touch, gestures, declarative-ui, state, binding, observable, remember, state-hoisting, recomposition, mvvm, viewmodel, unidirectional-data-flow, udf, single-source-of-truth, layers, repository, persistence, swiftdata, core-data, room, sqlite, datastore, userdefaults, keychain, networking, urlsession, retrofit, ktor, async-await, actors, main-actor, coroutines, flow, structured-concurrency, offline-first, sync, conflict-resolution, background-work, workmanager, background-tasks, push-notifications, apns, fcm, deep-links, navigation, accessibility, react-native, expo, flutter, dart, kotlin-multiplatform, compose-multiplatform, pwa, cross-platform-tradeoffs, testing, xctest, espresso, release, ci, app-size]
sources: [mobile-development-courses]
summary: Mobile apps run under constraints servers and browsers don't — the OS can suspend or kill the process at any moment (so state must be saved and restored and every screen must be reconstructable from persisted or fetched data), memory, battery and radio are budgeted (batch network work, avoid wakeups, respect background execution limits), every capability is behind a permission and a sandbox, distribution goes through store review with slow rollout and no instant rollback, devices fragment by size/OS version/performance, and input is touch on a small screen — and both platforms answered the UI problem the same way: SwiftUI and Jetpack Compose describe the UI as a function of state (a `View`/`@Composable` re-evaluated when the state it reads changes), with local state (`@State`/`remember`), state passed down and mutations passed up (`@Binding`/state hoisting), observable models (`@Observable`/`ViewModel` + `StateFlow`), and unidirectional data flow into a layered architecture (UI ← ViewModel ← repository ← local database and network) where the local database is the single source of truth for an offline-first app that syncs in the background and reconciles conflicts explicitly; persistence uses SwiftData/Core Data or Room over SQLite plus key-value stores (UserDefaults/DataStore) and the Keychain for secrets, networking and concurrency use Swift's async/await with actors (UI on the main actor) or Kotlin coroutines and Flow with structured concurrency, background work goes through the platforms' schedulers (BGTaskScheduler, WorkManager) because apps can't run freely in the background, and push arrives via APNs/FCM; cross-platform frameworks trade native fidelity and platform-feature latency for one codebase — React Native (JS/React rendering native views via JSI/Fabric, Expo tooling), Flutter (Dart, own renderer, pixel-identical everywhere), Kotlin Multiplatform (share logic, keep native UI), and PWAs (no store, limited APIs) — and the choice depends on team skills, how platform-specific the UI must be, and performance needs; testing spans unit tests of ViewModels, UI tests (XCTest/Espresso/Compose test), device farms, and staged store rollouts with crash reporting.
---
# Mobile development and cross-platform

**In one sentence.** A mobile app is a state machine the OS may kill at any time,
running on a battery, behind permissions, distributed through a store — so design for
restoration and offline first, keep the UI a pure function of state (which both SwiftUI
and Compose now enforce), and choose native vs cross-platform by how much the platform
itself is your product.

## What makes mobile different (Apple/Android lifecycle docs; HIG; Android quality guide)
**Lifecycle**: iOS states — not running, inactive, active, background (seconds to
finish work), suspended (frozen; may be terminated without notice); Android — Activity
`onCreate → onStart → onResume → onPause → onStop → onDestroy`, plus **process death**
when the system reclaims memory (the app restarts with `savedInstanceState`; a
ViewModel survives configuration changes like rotation but not process death). Design
consequence: every screen must be reconstructable from persisted state + navigation
arguments; never keep the only copy of user input in memory; save early. **Resources**:
memory warnings (`didReceiveMemoryWarning`, `onTrimMemory`), **battery** (radio and GPS are
the drains — batch and defer network, avoid periodic polling, use push;
[[web-performance-and-browser-networking]] RRC), **background execution** is restricted
(iOS background modes/`BGTaskScheduler`, Android `WorkManager` with constraints and
Doze/App Standby) — you schedule work, the OS runs it when it chooses. **Permissions
and sandbox**: each app in its own container; runtime permissions with rationale
(location, camera, contacts, notifications), privacy manifests/labels, App Tracking
Transparency; least privilege and ask in context. **Distribution**: App Store/Play
review (days), staged rollouts, no instant rollback (feature flags and server-side kill
switches instead — [[continuous-integration-and-delivery]]), old versions live for
years (API compatibility — [[api-design]]), app size limits and download costs.
**Fragmentation**: screen sizes/densities, notches/safe areas, foldables, OS versions
(Android especially), performance tiers, locales/RTL, dark mode, Dynamic Type/font
scaling, accessibility (VoiceOver/TalkBack — semantics on every control). **Input**:
touch targets ≥ 44 pt, gestures (tap, long press, swipe, pinch — conflicts with
scrolling), keyboard avoidance, haptics; platform conventions (HIG vs Material:
navigation stacks vs back gesture, tab bars, sheets) — users notice foreign idioms.

## Declarative UI: SwiftUI and Compose (CS193p L1–8 — read; Compose docs)
Both replaced imperative view hierarchies (UIKit/Views XML + manual updates) with
**UI = f(state)** ([[frontend-frameworks-and-state-management]]):
- **SwiftUI**: `struct ContentView: View { @State private var count = 0; var body: some
  View { VStack { Text("\(count)"); Button("Tap") { count += 1 } } } }` — `body` is
  re-evaluated when any `@State`/observed value it reads changes; views are cheap value
  types (structs), the framework diffs and updates the render tree; **`@State`** (view-
  owned source of truth), **`@Binding`** (a reference to someone else's state — two-way
  child edits), **`@Observable`** classes (iOS 17; earlier `ObservableObject` +
  `@Published` + `@StateObject`/`@ObservedObject`), **`@Environment`** for injected
  values; **view modifiers** compose (`.padding().background()` — order matters);
  layout: parent proposes a size, child chooses, parent positions (`HStack/VStack/
  ZStack`, `Spacer`, `GeometryReader`, `Layout`); `ForEach` over `Identifiable`;
  `NavigationStack` with typed paths; animation by declaring what changes
  (`withAnimation`, implicit `.animation`, matched geometry); Swift's type system
  (protocols with associated types, generics, `some View`, enums with payloads,
  Optionals — CS193p L3, L7, L9) does the heavy lifting.
- **Jetpack Compose**: `@Composable fun Counter() { var count by remember { mutableStateOf
  (0) }; Button(onClick = { count++ }) { Text("$count") } }` — **recomposition** re-runs
  composables whose read state changed (skipping stable ones); **`remember`** keeps
  state across recompositions, `rememberSaveable` across process death; **state
  hoisting** (stateless composables taking `value` + `onValueChange`) is the
  props-down/events-up rule; `LaunchedEffect`/`DisposableEffect` for side effects with
  keys; `Modifier` chains (order matters); Material 3 components; `LazyColumn` with
  keys; Navigation Compose with typed routes; adaptive layouts via window size classes.
- Shared discipline: keep composables/views pure and cheap, hoist state to the level
  that needs it, derive rather than duplicate, keep expensive work out of the render
  path, give lists stable identity.

## Architecture, persistence, concurrency (Android "Guide to app architecture"; CS193p L3–4, L13–14)
**Layers**: UI (views + **ViewModel** holding UI state as an immutable state object /
`StateFlow`, surviving rotation) ← domain (optional use cases) ← **data** (repositories
that arbitrate between local DB and network and expose Flows/AsyncSequences); **unidirectional
data flow**: events up (`viewModel.onAddTapped()`), state down (`uiState`); **single source of
truth**: the local database, not the last network response. **Persistence**: **SwiftData**
(`@Model` classes, `ModelContainer/Context`, `#Predicate`, relationships — CS193p L13–14;
built on Core Data) or Core Data; **Room** (annotated entities/DAOs over SQLite, Flow
queries, migrations); raw SQLite/GRDB/SQLDelight; key-value: `UserDefaults`/`DataStore`
(preferences); **Keychain**/EncryptedSharedPreferences for secrets — never plain files;
files in the sandbox with backup flags; iCloud/Google Drive sync where wanted. **Concurrency**:
Swift `async/await`, `Task`, **actors** (data isolation; `@MainActor` for UI — compiler-
checked in Swift 6 strict concurrency), `AsyncSequence`; Kotlin **coroutines**
(`viewModelScope.launch`, `Dispatchers.IO/Main`), **structured concurrency** (cancel with
scope), `Flow`/`StateFlow` for streams; never block the main thread (jank at 16 ms;
ANR at 5 s on Android — [[processes-and-threads]]). **Networking**: `URLSession`/Retrofit/
Ktor + `Codable`/kotlinx.serialization; certificate pinning where warranted; retries
with backoff and reachability awareness ([[microservices-and-resilience-patterns]]);
image loading/caching libraries (Kingfisher/Coil). **Offline-first**: write to the local
DB immediately (optimistic), queue mutations, **sync** in background with idempotent
server APIs, resolve **conflicts** explicitly (last-writer-wins with timestamps,
server-authoritative, per-field merge, or CRDT-style for collaborative data —
[[consistency-models]]); show sync state in the UI. **Push**: APNs/FCM tokens registered
with your backend; silent pushes to trigger sync; notification permissions and
categories; deep links/universal links into app state.

## Cross-platform: React Native, Flutter, KMP, PWA (docs; CS50 Mobile)
- **React Native**: React components render *native* widgets; JS runs on a separate
  thread talking to native through **JSI**/Fabric (new architecture replaces the async
  bridge); **Expo** provides tooling, OTA JS updates (within store rules), and modules;
  strengths — web-team skills, one codebase, native look; weaknesses — bridging cost
  for heavy native APIs, dependency on community modules, startup and list performance
  needs care (`FlatList`/FlashList), debugging across two worlds.
- **Flutter**: Dart compiled AOT; draws every pixel with its own engine (Skia/**Impeller**) —
  identical rendering everywhere and 60/120 fps animations; widgets for Material and
  Cupertino; strengths — consistency, performance, tooling (hot reload); weaknesses —
  non-native feel unless carefully mimicked, accessibility/platform-widget gaps,
  app size, Dart as an extra language.
- **Kotlin Multiplatform** (+ Compose Multiplatform): share business logic, networking,
  persistence (SQLDelight), keep SwiftUI/Compose UIs (or share Compose UI); the "share
  what's platform-agnostic" middle path favoured by Android-heavy teams.
- **PWA** ([[web-performance-and-browser-networking]] service workers): no store gate,
  instant updates, one web codebase; limited APIs (especially iOS: push only recently,
  no background sync), discoverability, offline via Cache API.
- Others: .NET MAUI, Ionic/Capacitor (web view + native plugins), Unity for games.
**Choosing**: native when the platform experience *is* the product (camera, AR, widgets,
complex gestures, latest OS features on day one, top-tier performance); cross-platform
when the app is mostly forms/lists/content, the team is small or web-skilled, and time
to market on both stores matters; hybrid (native shell + shared logic via KMP, or native
+ web views for content) is common. Expect platform-specific code either way (10–30 %).

## Testing and release
Unit-test ViewModels/repositories (pure logic; fake data sources — [[unit-testing]]);
UI tests (XCTest UI, Espresso, Compose testing, Detox/Maestro for RN); snapshot tests;
device farms (Firebase Test Lab, AWS Device Farm) across OS versions; profiling
(Instruments, Android Profiler — startup time, jank, memory, battery); crash reporting
(Crashlytics/Sentry) and ANR/hang monitoring; **CI** (Fastlane, Xcode Cloud, Gradle;
signing and provisioning as code — [[continuous-integration-and-delivery]]); **release**:
TestFlight/internal testing tracks → staged rollout (1 % → 100 %) watching crash-free
rate → halt if needed; feature flags server-side; semantic app versions; minimum OS
support policy; App Store review guidelines and Play policies (privacy, permissions,
payments) as hard constraints; app size (asset catalogs/thinning, App Bundles, dynamic
delivery); localization and accessibility audits before launch.

## Pitfalls
- Assuming the process stays alive; state only in memory; not handling restoration.
- Blocking the main thread (network, DB, JSON parsing on the UI thread); ANRs.
- Polling in the background; ignoring Doze/background limits; waking the radio often.
- Network response as source of truth → broken offline; silent sync conflicts.
- Requesting all permissions at launch; secrets in UserDefaults/SharedPreferences.
- Choosing cross-platform for a UI-heavy app and then rewriting native widgets by hand.

## Related
- [[frontend-frameworks-and-state-management]], [[web-performance-and-browser-networking]],
  [[javascript-and-the-event-loop]] (React Native), [[processes-and-threads]],
  [[consistency-models]] (sync/conflicts), [[api-design]], [[microservices-and-resilience-patterns]],
  [[continuous-integration-and-delivery]], [[unit-testing]], [[html-css-and-the-dom]]
  (accessibility parallels), [[human-computer-interaction]].

## Sources
Hegarty, CS193p Spring 2025 (read: lecture list) and 2020–23; Google, *Android Basics with Compose* (read: site) and "Guide to app architecture", "Background work overview"; Apple, "Managing your app's life cycle", Human Interface Guidelines, Swift Concurrency docs; Kotlin coroutines guide; React Native docs (new architecture), Expo docs; Flutter architectural overview; Kotlin Multiplatform docs; CS50 Mobile.
