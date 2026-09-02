---
title: Mobile & cross-platform — Stanford CS193p Developing Apps for iOS (SwiftUI, 2025; lecture list read), Google's Android Basics with Compose (free; site read), CS50 Mobile (React Native), Apple Human Interface Guidelines and Android app-architecture guidance, React Native and Flutter documentation, Kotlin Multiplatform
type: source
section: "7.6"
level: 300
tags: [cs193p, stanford, swiftui, ios, hegarty, android-basics, jetpack-compose, kotlin, android, cs50-mobile, react-native, flutter, dart, kotlin-multiplatform, kmp, human-interface-guidelines, hig, material-design, app-architecture, mvvm, swiftdata, declarative-ui, mobile]
sources: []
authors: [Paul Hegarty, Google Android Developers, Apple Developer, Meta, Google Flutter team]
year: 2025
institution: Stanford / Google / Apple / Harvard
url: https://cs193p.stanford.edu/
license: open videos and docs
format: html
summary: CS193p (Spring 2025; lecture list read) teaches iOS with SwiftUI through one app (CodeBreaker): Xcode and Views, view modifiers, separating the Model (logic and data) from the UI and the Swift type system, @State and Optionals, layout and data flow ("intro to functional programming"), generics and ViewBuilder, @Binding, animation, elapsed time and protocols, List and navigation (ForEach, Hashable, Identifiable), iPad and sheets, editors, and SwiftData persistence (@Model, @Relationship, ModelContainer/ModelContext, FetchDescriptor, #Predicate); Android Basics with Compose (site read) covers Kotlin, Compose UI, adaptive layouts across phones/tablets/foldables/Wear/TV/cars, app architecture (UI layer, domain, data layer; ViewModel; navigation; modularization; testing), Kotlin Multiplatform, and app-quality guidance (accessibility, performance, security, permissions, identity); CS50 Mobile uses React Native; Apple's Human Interface Guidelines and Material Design set platform conventions; and the cross-platform options are React Native (JS/React over native views), Flutter (Dart, its own rendering engine), and Kotlin Multiplatform (shared logic, native UI).
---
# Mobile & cross-platform: sources

## What they are
- **CS193p** (Hegarty; read: 2025 lecture list): L1–2 SwiftUI Views and modifiers; L3–4
  Model vs UI, Swift type system, `@State`, Optionals; L5–6 layout and data flow; L7–8
  generics, `ViewBuilder`, `@Binding`, animation; L9 protocols; L10 `List`, navigation,
  `Identifiable`/`Hashable`; L11–12 iPad, sheets, editors; L13–14 SwiftData persistence;
  later lectures typically cover networking/async, gestures, and the App Store. Earlier
  years (2020–23) cover MVVM with `ObservableObject`, `@Published`, `@EnvironmentObject`,
  Combine, `Codable`, `UserDefaults`, drawing with `Shape`/`GeometryReader`.
- **Android Basics with Compose** (read: developer site structure): units on Kotlin
  basics, Compose UI (composables, state hoisting, `remember`, recomposition), layouts
  and Material 3, navigation, architecture (ViewModel, UI state, repository, Room,
  DataStore, WorkManager), connectivity (Retrofit/Ktor, coroutines/Flow), adaptive
  layouts, testing; plus the "Guide to app architecture" (UI/domain/data layers,
  unidirectional data flow, single source of truth) and quality/security/permissions
  guides.
- **CS50 Mobile** (Harvard; React Native, JS, Expo). **Docs**: Apple HIG (platform
  conventions, navigation, gestures, accessibility), Material Design 3; React Native
  (bridge → JSI/Fabric new architecture; Expo), Flutter (widgets, Skia/Impeller
  renderer, Dart isolates), Kotlin Multiplatform / Compose Multiplatform.

## Key ideas → pages
[[mobile-development-and-cross-platform]]; related existing:
[[frontend-frameworks-and-state-management]], [[web-performance-and-browser-networking]].

## What they add
Two platforms that independently converged on the same declarative, state-driven UI
model as React (SwiftUI 2019, Compose 2021), and a course that teaches it through one
evolving app — the best evidence that "UI = f(state)" is now the industry's shared model.
