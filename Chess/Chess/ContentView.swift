//
//  ContentView.swift
//  Chess
//
//  Created by Kaede Sugano on 19/12/2023.
//

import SwiftUI

let screenWidth = UIScreen.main.bounds.width
let screenHeight = UIScreen.main.bounds.height

enum ChessSide {
    case white, black
}

struct ContentView: View {
    
    var body: some View {
        NavigationView {
            VStack {
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack {
                        Text("aaa")
                            .foregroundColor(Color("historybartxt"))
                    }
                }
                .background(Color("historybar"))
                .frame(height: screenHeight * 0.02)
                
                Spacer()
                
                ChessboardView(screenWidth: screenWidth, side: .white)
                
                Spacer()
            }
            .background(Color("background"))
            .navigationBarTitle("Chess", displayMode: .inline)
            .navigationBarColor(Color("navbar"))
        }
        .tabBarView()
    }
}

extension View {
    func navigationBarColor(_ backgroundColor: Color) -> some View {
        let uiColor = UIColor(backgroundColor)
        return self.modifier(NavigationBarModifier(backgroundColor: uiColor))
    }
}

struct NavigationBarModifier: ViewModifier {
    
    var backgroundColor: UIColor?
    var titleColor: UIColor?
    
    init(backgroundColor: UIColor?, titleColor: UIColor? = .white) {
        self.backgroundColor = backgroundColor
        self.titleColor = titleColor
        
        let coloredAppearance = UINavigationBarAppearance()
        coloredAppearance.configureWithOpaqueBackground()
        coloredAppearance.backgroundColor = backgroundColor
        coloredAppearance.titleTextAttributes = [.foregroundColor: titleColor ?? .white]
        coloredAppearance.largeTitleTextAttributes = [.foregroundColor: titleColor ?? .white]
        
        UINavigationBar.appearance().standardAppearance = coloredAppearance
        UINavigationBar.appearance().compactAppearance = coloredAppearance
        UINavigationBar.appearance().scrollEdgeAppearance = coloredAppearance
    }
    
    func body(content: Content) -> some View {
        ZStack {
            content
        }
    }
}

extension View {
    func tabBarView() -> some View {
        self.modifier(TabBarModifier())
    }
}

struct TabBarModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .toolbar {
                ToolbarItemGroup(placement: .bottomBar) {
                    Button(action: {}) {
                        Image(systemName: "house")
                    }
                    Spacer()
                    Button(action: {}) {
                        Image(systemName: "magnifyingglass")
                    }
                    Button(action: {}) {
                        Image(systemName: "person")
                    }
                }
            }
            .background(Color("navbar"))
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}