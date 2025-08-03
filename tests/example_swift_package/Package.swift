// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "MujaTools",
    platforms: [
        .macOS(.v12),
        .iOS(.v15)
    ],
    products: [
        .library(name: "MujaCore", targets: ["MujaCore"]),
    ],
    dependencies: [
        .package(url: "https://github.com/apple/swift-argument-parser", from: "1.2.0")
    ],
    targets: [
        .target(
            name: "MujaCore",
            dependencies: [.product(name: "ArgumentParser", package: "swift-argument-parser")]
        ),
        .testTarget(
            name: "MujaCoreTests",
            dependencies: ["MujaCore"]
        )
    ]
)

